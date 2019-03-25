import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d


class Model:
    
    def __init__(self, converter, policies, mutator, crossover, scaler=None):
        self._converter = converter
        self._policies = policies
        self._scaler = scaler
        self._mutator = mutator
        self._crossover = crossover

        self._func = None
        self._population = None   
        self._arg_num = None
        self._axes = None
        self._digits = None

        self._cache = {}
    
    @property
    def converter(self):
        return self._converter.__name__
    
    @property
    def policies(self):
        include = self._policies['include'].__name__
        exclude = self._policies['exclude'].__name__
        parents = self._policies['parents'].__name__
        
        return 'include: {}\nexclude{}\nparents:{}'.format(include, exclude, parents)
    
    @property
    def scaler(self):
        return self._scaler.__name__
        
    @property
    def mutator(self):
        return self._mutator.__name__
    
    @property
    def crossover(self):
        return self._crossover.__name__
   
    @property
    def population(self):
        return self._population
    
    def run(self, func, *intervals, n=20, eps=0.01):
        """
            Run algorithm.

            func:function - function to optimize.
            intervals:[(float)] - intervals for each variable where we optimize our function.
            n:int - population volume.
            eps:float - accuracy of the algorithm.
        """   
        
        assert self._converter is not None, 'Converter is not found.'
        assert self._policies is not None, 'Policies is not found.'
        assert self._mutator is not None, 'Mutator operator is not found.'
        assert self._crossover is not None, 'Crossover operator is not found.'

        self._func = func
        self._arg_num = func.__code__.co_argcount

        assert self._arg_num == len(intervals)

        self._axes = [list(np.arange(a, b, eps)) for a, b in intervals]

        max_len = max([len(ax) for ax in self._axes])

        self._digits = int(np.ceil(np.log2(max_len)))

        self._population = [list(np.random.choice(ax, size=n)) for ax in self._axes]

        self._population = list(zip(*self._population))

    def _to_genes(self, x, scope):
        """
        Converts x value to gene representation.

        :param x:float - value.
        :param scope:[float] - scope where x could be.
        :return:[bool] - gene representation/
        """

        x = scope.index(x)
        x = self._converter.convert(x, self._digits)

        return x

    def _to_float(self, x, scope):
        """
        Converts x gene representation to its value.

        :param x:[bool] - gene representation.
        :param scope:[float] - scope where x could be
        :return:float - value.
        """

        x = self._converter.to_int(x)
        x = min(x, len(scope) - 1)
        x = scope[x]

        return x

    def _caching(self, t):
        """
        Cache data for future ploting and other activities.

        :param t:int - time-step when we use caching.
        :return:None
        """

        self._cache[t] = self._population[:]

    def plot(self):
        """
        Plot evolution.

        :return: None
        """

        for key, value in self._cache.items():
            eps = 0.0001
            x = [key] * len(value)
            y = [self._func(*i) for i in value]
            #size = [np.sqrt(abs(i)) + eps for i in y]

            plt.scatter(x, y, label='Epoch: {}'.format(key))

        plt.xlabel('epoch')
        plt.ylabel('function value')
        plt.legend()
        plt.show()

    def plot_graph(self):
        """
        Plot function graph depending on the number of values.

        :return: None
        """

        assert self._arg_num in (1, 2)

        if self._arg_num == 1:
            self.plot1D()
        elif self._arg_num == 2:
            self.plot2D()

    def plot1D(self):
        """
        Plot function graph.

        :return: None
        """

        assert self._arg_num == 1, 'Function must be 1-dimensional'

        x = self._axes[0]
        y = [self._func(i) for i in x]
        plt.plot(x, y)

        max_key = max(self._cache.keys())
        min_key = min(self._cache.keys())
        for key, value in self._cache.items():
            color = 1 - (key - min_key) / (max_key - min_key)
            x = [i[0] for i in value]
            y = [self._func(i) for i in x]
            plt.scatter(x, y, c=str(color), label='Epoch: {}'.format(key))

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.show()

    def plot2D(self):
        """
        Plot function graph.

        :return: None
        """

        assert self._arg_num == 2, 'Function must 2-dimensional.'

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x, y = self._axes
        X, Y = np.meshgrid(x, y)
        Z = self._func(X, Y)
        ax.plot_surface(X, Y, Z)

        max_key = max(self._cache.keys())
        min_key = min(self._cache.keys())
        for key, value in self._cache.items():
            X, Y, Z = [], [], []
            for x, y in value:
                X.append(x)
                Y.append(y)
                Z.append(self._func(x, y))

            color = 1 - (key - min_key) / (max_key - min_key)

            ax.scatter(X, Y, Z, c=str(color), label='Epoch: {}'.format(key))

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('f(x, y)')
        ax.legend()

        plt.show()


