# coding=utf-8
import logging

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import TSPGenotype

logger = logging.getLogger(__name__)


class TSPEvaluator(Operator):
    def __init__(self):
        super(TSPEvaluator, self).__init__(TSPGenotype)

    def process(self, population):
        for genotype in population:
            genotype.fitness = genotype.calculate_fitness()
