# import numpy as np
class Scale:

    @staticmethod
    def linear(a, b):
        """ 
            F_scale = a * F + b
            F_scale > (1.2 - 2.0) * F
            
            func:func - function to scale.
            a:float - parameter.
            b:float - parameter.
        """
        def scaled_func(f):
            return lambda x, y: a * f(x, y) + b

        return scaled_func

    #
    # @staticmethod
    # def sigma(c=1):
    #     """
    #         F_scale = F + (F_mean - c * sigma)
    #         F_mean - average population fitness at its initial generation.
    #         sigma - standard deviation of individual species by population
    #
    #         func:function - function to scale.
    #         population:[float] - population.
    #         c:int - parameter. cє[1, 5]
    #     """
    #     mean = np.mean(initial_fitness)
    #     def scale(func, population):
    #         sigma = np.std(population)
    #         return lambda x: func(x) + (mean - c * sigma)
    #
    #     return scale

    @staticmethod
    def power(y):
        """
            F_scale = F ** y
            
            func:function - function to scale.
            y:float - parameter. y >~ 1
        """

        def scaled_func(f):
            return lambda x, y: a * f(x, y) + b

        return scaled_func