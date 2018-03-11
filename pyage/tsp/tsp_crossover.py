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
        logger.debug("Crossing: " + str(p1) + " and " + str(p2))

        parent1_order = list(p1.order)
        parent2_order = list(p2.order)

        index1 = random.randrange(0, len(parent1_order))
        index2 = random.randrange(0, len(parent1_order))
        if index1 > index2:
            index1, index2 = index2, index1

        parent1_order_part = parent1_order[index1:index2]

        for city in parent1_order_part:
            parent2_order.remove(city)

        child_order = parent1_order_part + parent2_order

        genotype = TSPGenotype(p1.points)
        genotype.set_order(child_order)

        logger.debug("Crossed genotype: " + str(genotype))

        return genotype
