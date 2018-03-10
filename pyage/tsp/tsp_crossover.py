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

        parent1 = list(p1.points)
        parent2 = list(p2.points)

        index1 = random.randrange(0, len(parent1))
        index2 = random.randrange(0, len(parent1))
        if index1 > index2:
            index1, index2 = index2, index1

        parent1fragment = parent1[index1:index2]
        parent2fragment = parent2

        for city in parent1fragment:
            parent2fragment.remove(city)
        genlist = parent1fragment + parent2fragment

        genotype = TSPGenotype(genlist)

        logger.debug("Crossed genotype: " + str(genotype))

        return genotype
