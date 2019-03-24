import numpy as np


class Operator:

    @staticmethod
    def mutate():
        """
            Changes random gene to another value

            gene:[bool]: list of genes.
        """

        def func(gene):
            idx = np.random.randint(len(gene))
            gene[idx] = not gene[idx]
            return gene

        return func

    @staticmethod
    def inverse():
        """
            Changes two random parts of gene with each other.
            
            gene:[bool]: list of genes.
        """

        def func(gene):
            idx = np.random.randint(1, len(gene))

            return gene[idx:] + gene[:idx]

        return func

    @staticmethod
    def crossover():
        """
            Every gene divides in the same position.
            The their parts changes with each other resulting offsprings.
            
            gene_a:[bool]: list of genes.
            gene_b:[bool]: list of genes.
        """

        def func(*args):
            gene_a, gene_b = args

            idx = np.random.randint(1, len(gene_a))
            offspring_a = gene_a[:idx] + gene_b[idx:]
            offspring_b = gene_b[:idx] + gene_a[idx:]

            return [offspring_a, offspring_b]

        return func
