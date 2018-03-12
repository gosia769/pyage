import sys

import logging

from pyage.tsp.tsp_mutation import TSPRandomMutation, TSPConsecutiveMutation

logger = logging.getLogger(__name__)


def get_arguments():
    args = sys.argv

    if len(args) < 7:
        raise ValueError("Not enough parameters!")

    return Arguments(args[3] == 'True', float(args[4]), args[5], args[6])


class Arguments:
    def __init__(self, emas, mutation_probability, mutation_fun, filename):
        self.filename = filename
        self.mutation_probability = mutation_probability
        self.mutation_type = TSPRandomMutation(self.mutation_probability)\
            if mutation_fun == "random"\
            else TSPConsecutiveMutation(self.mutation_probability)
        self.emas = emas
        self.logParameters()

        self.emas_str = "EMAS" if emas else "EVO"
        self.mutation_str = mutation_fun
        self.probability_str = str(mutation_probability)

    def logParameters(self):
        logger.info("Emas: " + str(self.emas))
        logger.info("Mutation: " + str(self.mutation_type))
        logger.info("Probability: " + str(self.mutation_probability))
        logger.info("Filename: " + str(self.filename))
