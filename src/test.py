from models import Elit
from utils.converter import Converter
from utils.operators.basic import Operator as op
from utils.operators.modified import Operator as op_m
from utils.policies import Policy

import numpy as np

converter = Converter(type_='grey')
crossover = op.crossover()
mutator = op_m.Mutate.multi(3)
policies = {
    'include': Policy.elitarium(),
    'exclude': Policy.elitarium(),
    'parents': Policy.random()
}

func = lambda x, y: x ** 2 + y ** 2
interval_x = interval_y = (-10, 11)
n = 100
eps = 1

model = Elit(converter=converter, policies=policies, mutator=mutator, crossover=crossover)
model.run(func, interval_x, interval_y, epochs=1000, n=50, eps=eps, optimize='min', t=10, verbose=True)
model.plot()
model.plot_graph()