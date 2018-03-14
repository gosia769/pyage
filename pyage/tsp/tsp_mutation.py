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
        logger.debug("Random mutation of {0}".format(str(genotype)))

        n = len(genotype.order)
        new_gen = TSPGenotype(genotype.points, order=swap(list(genotype.order),
                                                          random.randrange(n),
                                                          random.randrange(n)))

        logger.debug("Mutated {0}".format(str(new_gen)))
        return new_gen


class TSPConsecutiveMutation(AbstractMutation):
    def __init__(self, probability):
        super(TSPConsecutiveMutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Consecutive mutation of {0}".format(str(genotype)))

        n = len(genotype.order)
        random_choice = random.randrange(n)
        new_gen = TSPGenotype(genotype.points,
                              order=swap(list(genotype.order), random_choice,
                                         (random_choice + 1) % n))

        logger.debug("Mutated {0}".format(str(new_gen)))
        return new_gen


class TSPInverseMutation(AbstractMutation):
    def __init__(self, probability):
        super(TSPInverseMutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Inverse mutation of {0}".format(str(genotype)))

        new_gen = TSPGenotype(genotype.points, order=inverse(genotype.order))

        logger.debug("Mutated {0}".format(str(new_gen)))
        return new_gen


def swap(order, index1, index2):
    order[index1], order[index2] = order[index2], order[index1]
    return order


def inverse(s):
    x, y = random.sample(range(len(s)), 2)
    if x > y:
        x, y = y, x
    return s[:x + 1] + s[y - 1:x:-1] + s[y:]
