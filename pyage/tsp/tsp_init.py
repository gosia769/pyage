import pandas as pd
from pyage.tsp.tsp_genotype import TSPGenotype

from pyage.core.emas import EmasAgent
from pyage.core.inject import Inject
from pyage.tsp.point import Point


class EmasInitializer(object):
    def __init__(self, filename, energy, size):
        self.filename = filename
        self.points = []
        self.initialize_points()
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

    def initialize_points(self):
        point_pandas = pd.read_csv(self.filename)
        for point_series in point_pandas.iterrows():
            self.points.append(
                Point(point_series[0], point_series[1].X, point_series[1].Y))
