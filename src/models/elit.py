import numpy as np
from tqdm import tqdm

from .model import Model


class Elit(Model):

    def __init__(self, converter, policies, mutator, crossover, scaler=None):
        super().__init__(converter, policies, mutator, crossover, scaler)

    def run(self, func, *intervals, epochs=1000, p=0.05, n=20, eps=0.01, optimize='max', t=100, verbose=True):
        """
            Run algorithm.

            func:function - function to optimize.
            intervals:[(float)] - interval for each variable where we optimize our function.
            epochs:int - number of epochs.
            p:float - probability of mutattion. 0 < p < 1
            n:int - population volume.
            eps:float - accuracy of the algorithm.
            optimize:str - whether to maximize or minimize. ['max', 'min']
            parents_amount:int - only for multichromosomal crossover.
            t:int - time-step when we use caching and verbose
            verbose:bool - whether to verbose.
            cache:bool - whether to cache.
        """

        super().run(func, *intervals, n=n, eps=eps)

        for i in range(epochs):

            if i % t == 0:
                if verbose:
                    print('_' * 50)
                    print('Iteration {}.'.format(i))
                    print('Population:\n{}'.format(self._population))
                self._caching(i)

            # Get parents
            parents = self._policies['parents'](self._population, size=2,
                                                func=func, optimize=optimize, best=True)

            # Get parents' genes.
            parents_genes = [[self._to_genes(parent[ax], self._axes[ax]) for ax in range(len(parent))]
                             for parent in parents]

            # Get offspring using crossover operator
            offsprings_genes = [self._crossover(x, y) for x, y in zip(*parents_genes)]
            offsprings_genes = list(zip(*offsprings_genes))

            # Convert gene representation to float
            offsprings = [[self._to_float(offspring[ax], self._axes[ax]) for ax in range(len(offspring))]
                          for offspring in offsprings_genes]

            # Get best offspring
            offspring = self._policies['include'](offsprings, func=func, optimize=optimize, best=True)[0]

            # Mutate offspring
            if np.random.random() < p:
                offspring = [self._to_genes(offspring[ax], self._axes[ax]) for ax in range(len(offspring))]
                offspring = [self._mutator(ax) for ax in offspring]
                offspring = tuple((self._to_float(offspring[ax], self._axes[ax]) for ax in range(len(offspring))))

            # Get worst individual
            worst_individual = self._policies['exclude'](self._population, func=func,
                                                         optimize=optimize, best=False)[0]

            # Get worst individual index
            worst_idx = self._population.index(worst_individual)

            # Change change worst individual to a new better offspring
            self._population[worst_idx] = offspring



