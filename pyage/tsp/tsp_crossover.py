# coding=utf-8
import logging
import random

from pyage.elect.el_crossover import AbstractCrossover
from pyage.tsp.tsp_genotype import TSPGenotype

logger = logging.getLogger(__name__)


class TSPCrossover(AbstractCrossover):
    def __init__(self, size):
        super(TSPCrossover, self).__init__(TSPGenotype, size)

    def cross(self, p1, p2):
        logger.debug("Crossing {0} and {1}".format(str(p1), str(p2)))

        p1_order = list(p1.order)
        p2_order = list(p2.order)
        points_size = len(p1_order)

        l = random.randrange(0, points_size)
        r = random.randrange(0, points_size)
        if l > r:
            l, r = r, l

        parent1_order_part = p1_order[l:r]

        for city in parent1_order_part:
            p2_order.remove(city)

        genotype = TSPGenotype(p1.points)
        genotype.set_order(parent1_order_part + p2_order)

        logger.debug("Crossed: {0}".format(str(genotype)))
        return genotype
