# coding=utf-8
import random
from itertools import tee


class TSPGenotype(object):
    def __init__(self, points):
        self.points = points
        self.number_of_points = len(points)
        self.order = [x for x in range(self.number_of_points)]
        random.shuffle(self.order)
        self.fitness = self.calculate_fitness()

    def __str__(self):
        return "TSPGenotype{order=" + str(self.order) + ", fitness=" + str(
            self.fitness) + "}"

    def calculate_fitness(self):
        fitness = 0.0
        for index1, index2 in pairwise(self.order):
            x_dist = self.points[index1].x - self.points[index2].x
            y_dist = self.points[index1].y - self.points[index2].y
            fitness -= x_dist ** 2 + y_dist ** 2
        return fitness

    def set_order(self, list):
        self.order = list[:]
        self.fitness = self.calculate_fitness()


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
