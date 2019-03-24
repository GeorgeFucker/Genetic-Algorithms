import numpy as np

from functools import reduce


class Converter:

    def __init__(self, type_):
        self.type_ = type_

    def convert(self, x, digits):
        """
        type_:str - ['bin', grey'].
        """

        if self.type_ is 'bin':
            return self.to_bin(x, digits)
        elif self.type_ is 'grey':
            return self.to_grey(x, digits)

    @staticmethod
    def to_bin(x, digits):
        """
            Converts 10-based bumber to 2-based number.
            
            x:int
        """

        x = bin(x)
        x = [bool(int(i)) for i in x[2:]]
        assert digits >= len(x)
        x = [False] * (digits - len(x)) + x

        return x

    @staticmethod
    def to_grey(x, digits):
        """
            Converts 10-based number to grey number.
            
            x:int
        """

        x = bin(x)
        x = [bool(int(i)) for i in x[2:]]
        x = [False] + x
        x = [x[i] ^ x[i + 1] for i in range(len(x) - 1)]
        assert digits >= len(x)
        x = [False] * (digits - len(x)) + x

        return x

    def to_int(self, x):
        """
            Converts 2-based bumber or grey number to 10-based number.
            
            x:int
            from_:str - type of x
        """

        if self.type_ is 'bin':
            x = [str(int(n)) for n in x]
            x = '0b' + ''.join(x)
        elif self.type_ is 'grey':
            x = [
                str(int(False ^ reduce(np.logical_xor, x[:i + 1])))
                for i in range(len(x))
            ]

            x = '0b' + ''.join(x)

        return int(x, 2)
