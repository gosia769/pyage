import pandas as pd

from pyage.core.emas import EmasAgent
from pyage.core.inject import Inject
from pyage.core.operator import Operator
from pyage.tsp.point import Point
from pyage.tsp.tsp_genotype import TSPGenotype


class EmasInitializer(object):
    def __init__(self, filename, energy, size):
        self.filename = filename
        self.points = initialize_points(self.filename)
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(TSPGenotype(self.points), self.energy,
                              self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


def initialize_points(filename):
    points = []
    point_pandas = pd.read_csv(filename)
    for point_series in point_pandas.iterrows():
        points.append(
            Point(point_series[0], point_series[1].X, point_series[1].Y))
    return points


class TSPInitializer(Operator):
    def __init__(self, population_size=1000, filename=None):
        super(TSPInitializer, self).__init__(TSPGenotype)
        self.size = population_size
        if filename:
            self.points = initialize_points(filename)
            self.population = [TSPGenotype(self.points) for _ in range(self.size)]

    def __call__(self, *args, **kwargs):
        return self.population

    def process(self, population):
        for i in range(self.size):
            population.append(self.population[i])
