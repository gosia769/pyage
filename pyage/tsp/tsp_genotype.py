import random
from itertools import tee, izip


class TSPGenotype(object):
    def __init__(self, points):
        self.points = points
        self.length = len(points)
        random.shuffle(self.points)
        self.fitness = self.calculate_fitness()

    def __str__(self):
        return "TSPGenotype{points=[" + str(
            list(map(lambda x: x.id, self.points))) + "], fitness=" + str(
            self.fitness) + "}"

    def calculate_fitness(self):
        fitness = 0.0
        for point1, point2 in pairwise(self.points):
            fitness -= (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2
        return fitness

    def set_list(self, points):
        self.points = list(points)
        self.fitness = self.calculate_fitness()


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)
