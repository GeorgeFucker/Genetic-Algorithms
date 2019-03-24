import numpy as np


class Policy:
    """
        Policies definition.
    """

    @staticmethod
    def random():
        """
            Chooses random individual. 
        """

        def select(population, size=1, **kwargs):
            indices = np.random.choice(range(len(population)), size, replace=False)
            result = [population[idx] for idx in indices]

            return result

        return select

    @staticmethod
    def elitarium():
        """
            Chooses individual with respect to its fitness function.
            
            func:function - function to optimize.
            optimize:str - whether to maximize or minimize.
            best:bool - whether to choose the best one or the worst.
        """

        def select(population, size=1, **kwargs):
            func = kwargs['func']
            optimize = kwargs['optimize']
            best = kwargs['best']

            fitness = [func(*args) for args in population]

            if (optimize is 'max' and best) or (optimize is 'min' and not best):
                indices = np.argsort(fitness)[-1: -1 - size: -1]
            else:
                indices = np.argsort(fitness)[:size]

            result = [population[idx] for idx in indices]

            return result

        return select

    @staticmethod
    def probabilistic(gamma=0.1, phi=None):
        """
            Selects individual with some probabilities which depend on fitness function.
            
            func:function - function to optimize.
            optimize:str - whether to maximize or minimize.
            best:bool - whether to choose the best one or the worst.
            gamma:float - reduction factor.
        """

        if phi:
            def select(population, size=1, **kwargs):
                func = kwargs['func']
                optimize = kwargs['optimize']
                best = kwargs['best']

                n = len(population)
                fitness = [func(*args) for args in population]
                fitness_sum = sum(fitness)
                fitness_min = (1 + phi) * min(fitness) - phi * max(fitness)
                fitness_max = (1 + phi) * max(fitness) - phi * min(fitness)

                if (optimize == 'max' and best) or (optimize == 'min' and not best):
                    prob = lambda x: (x - fitness_min) / (fitness_sum - n * fitness_min)
                else:
                    prob = lambda x: (fitness_max - x) / (n * fitness_max - fitness_sum)

                p = np.array([prob(fit) for fit in fitness])
                p = np.nan_to_num(p)
                denominator = len(p) - np.count_nonzero(p) if np.count_nonzero(p) else len(p)
                to_add = (1 - p.sum()) / denominator
                p = [x + (to_add if not x else 0) for x in p]

                indices = np.random.choice(range(len(population)), size, replace=False, p=p)
                result = [population[idx] for idx in indices]

                return result
        else:
            def select(population, size=1, **kwargs):
                func = kwargs['func']
                optimize = kwargs['optimize']
                best = kwargs['best']

                n = len(population)
                fitness = [func(*args) for args in population]
                fitness_sum = sum(fitness)
                fitness_min = min(fitness)
                fitness_max = max(fitness)

                if (optimize == 'max' and best) or (optimize == 'min' and not best):
                    Q = gamma * (fitness_sum - n * fitness_min) / ((1 - gamma) * n)
                    prob = lambda x: (x - fitness_min + Q) / (fitness_sum - n * (fitness_min - Q))
                else:
                    Q = gamma * (n * fitness_max - fitness_sum) / ((1 - gamma) * n)
                    prob = lambda x: (fitness_max - x + Q) / (n * (fitness_max + Q) - fitness_sum)

                p = np.array([prob(fit) for fit in fitness])
                p = np.nan_to_num(p)
                to_add = (1 - p.sum()) / len(p)
                p = [x + to_add for x in p]

                indices = np.random.choice(range(len(population)), size, replace=False, p=p)
                result = [population[idx] for idx in indices]

                return result

        return select
