from models import Elit
from utils.converter import Converter
from utils.operators.basic import Operator as op
from utils.operators.modified import Operator as op_m
from utils.policies import Policy
from utils.test_functions import ackley

import numpy as np

converter = Converter(type_='grey')
crossover = op.crossover()
mutator = op_m.Mutate.multi(3)
policies = {
    'include': Policy.elitarium(),
    'exclude': Policy.elitarium(),
    'parents': Policy.random()
}

n = 100
eps = 1

model = Elit(converter=converter, policies=policies, mutator=mutator, crossover=crossover)
model.run(*(ackley()), epochs=101, n=20, eps=eps, optimize='min', t=10, verbose=True)
model.plot()
model.plot_graph()