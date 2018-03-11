# coding=utf-8
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

        prev_order = list(genotype.order)
        index1 = random.randrange(0, len(prev_order))
        index2 = random.randrange(0, len(prev_order))
        prev_order[index1], prev_order[index2] = prev_order[index2], prev_order[index1]
        new_gen = TSPGenotype(genotype.points)
        new_gen.set_order(prev_order)

        logger.debug("Mutated (rand swap) genotype: " + str(new_gen))

        return new_gen


class TSPConsecutiveMutation(AbstractMutation):
    def __init__(self, probability):
        super(TSPConsecutiveMutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating (next swap) genotype: " + str(genotype))

        prev_order = list(genotype.order)
        index1 = random.randrange(0, len(prev_order))
        index2 = (index1 + 1) % len(prev_order)

        prev_order[index1], prev_order[index2] = prev_order[index2], prev_order[index1]

        new_gen = TSPGenotype(genotype.points)
        new_gen.set_order(prev_order)

        logger.debug("Mutated (next swap) genotype: " + str(new_gen))

        return new_gen
