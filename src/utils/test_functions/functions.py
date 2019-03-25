import numpy as np


def ackley():
    f = lambda x, y: -20 * np.exp(-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2))) - \
                     np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)) + np.pi + 20)
    interval_x = interval_y = (-5, 5)

    return f, interval_x, interval_y


def beale():
    f = lambda x, y: (1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + \
                     (2.625 - x + x * y ** 3) ** 2
    interval_x = interval_y = (-4.5, 4.5)

    return f, interval_x, interval_y


def goldstein_price():
    f = lambda x, y: (1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y **2)) * \
                     (30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2))
    interval_x = interval_y = (-2, 2)

    return f, interval_x, interval_y


def booth():
    f = lambda x, y: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2
    interval_x = interval_y = (-10, 10)

    return f, interval_x, interval_y


def bukin():
    f = lambda x, y: 100 * np.sqrt(abs(y - 0.01 * x ** 2)) + 0.01 * abs(x + 10)
    interval_x = (-15, -5)
    interval_y = (-3, 3)

    return f, interval_x, interval_y


def matyas():
    f = lambda x, y: 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
    interval_x = interval_y = (-10, 10)

    return f, interval_x, interval_y


def levi():
    f = lambda x, y: (np.sin(3 * np.pi * x)) ** 2 + (x - 1) ** 2 * (1 + (np.sin(3 * np.pi * y)) ** 2) + \
                     (y + 1) ** 2 * (1 + (np.sin(2 * np.pi * y)) ** 2)
    interval_x = interval_y = (-10, 10)

    return f, interval_x, interval_y


def himmelblau():
    f = lambda x, y: (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
    interval_x = interval_y = (-5, 5)

    return f, interval_x, interval_y


def three_hump_camel():
    f = lambda x, y: 2 * x ** 2 - 1.05 * x ** 4 + x ** 6 / 6 + x * y + y ** 2
    interval_x = interval_y = (-5, 5)

    return f, interval_x, interval_y


def easom():
    f = lambda x, y: -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi) ** 2 + (y - np.pi) ** 2))
    interval_x = interval_y = (-100, 100)

    return f, interval_x, interval_y


def cross_in_tray():
    f = lambda x, y: -0.0001 * (abs(np.sin(x) * np.sin(y) *
                                    np.exp(abs(100 - np.sqrt(x ** 2 + y ** 2) / np.pi))) + 1) ** 0.1
    interval_x = interval_y = (-10, 10)

    return f, interval_x, interval_y


def eggholder():
    f = lambda x, y: -(y + 47) * np.sin(np.sqrt(abs(x / 2 + (y + 47)))) - \
                     x * np.sin(np.sqrt(abs(x - (y + 47))))
    interval_x = interval_y = (-512, 512)

    return f, interval_x, interval_y


def holder_table():
    f = lambda x, y: -abs(np.sin(x) * np.cos(x) * np.exp(abs(1 - np.sqrt(x ** 2 + y ** 2) / np.pi)))
    interval_x = interval_y = (-10, 10)

    return f, interval_x, interval_y


def mccormick():
    f = lambda x, y: np.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1
    interval_x = (-1,5, 4)
    interval_y = (-3, 4)

    return f, interval_x, interval_y


def schaffer_2():
    f = lambda x, y: 0.5 + ((np.sin(x ** 2 - y ** 2)) ** 2 - 0.5) / \
                     (1 + 0.001 * (x ** 2 + y ** 2)) ** 2
    interval_x = interval_y = (-100, 100)

    return f, interval_x, interval_y


def schaffer_4():
    f = lambda x, y: 0.5 + ((np.cos(np.sin(abs(x ** 2 - y ** 2)))) ** 2 - 0.5) / \
                     (1 + 0.001 * (x ** 2 + y ** 2)) ** 2
    interval_x = interval_y = (-100, 100)

    return f, interval_x, interval_y