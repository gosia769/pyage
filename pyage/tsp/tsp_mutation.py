import logging
import random

from pyage.elect.el_mutation import AbstractMutation
from pyage.tsp.tsp_genotype import TSPGenotype

logger = logging.getLogger(__name__)


class TSPRandomMutation(AbstractMutation):
    def __init__(self, probability):
        super(TSPRandomMutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (rand swap) genotype: " + str(genotype))

        l = list(genotype.points)
        index1 = random.randrange(0, len(l))
        index2 = random.randrange(0, len(l))
        l[index1], l[index2] = l[index2], l[index1]
        gen = TSPGenotype(l)

        logger.debug("Mutated (rand swap) genotype: " + str(gen))

        return gen


class TSPConsecutiveMutation(AbstractMutation):
    def __init__(self, probability):
        super(TSPConsecutiveMutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (next swap) genotype: " + str(genotype))

        l = list(genotype.points)
        index1 = random.randrange(0, len(l))
        index2 = (index1 + 1) % len(l)
        l[index1], l[index2] = l[index2], l[index1]
        gen = TSPGenotype(l)

        logger.debug("Mutated (next swap) genotype: " + str(gen))

        return gen
