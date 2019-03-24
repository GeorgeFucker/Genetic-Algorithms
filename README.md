# Genetic-Algorithms

There is just one model of genetic algorithm. But I have ambitious to add more lately.
This is the most [simple model](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/models/elit.py) where better offsprings change the worst individuals in the population.

To create model you just need to give to it Converter, Mutator and Crossover objects as arguments and call method run() with appropriate arguments.
Also model requires policies as argument. Policies are methods which determines how we choose parents, offspring, etc.
Method run() shows changing of the population over time. Also you could see population changing over time using method [plot()](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/models/model.py).

To see example just look at [test.py](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/test.py).

Package utils has got [genetic operators](https://github.com/GeorgeFucker/Genetic-Algorithms/tree/master/src/utils/operators), [policies](https://github.com/GeorgeFucker/Genetic-Algorithms/tree/master/src/utils/policies) and Converter implementations.

[The Converter](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/utils/converter.py) is just a class which converts integer numbers into binary or grey representations and vice versa with appropriate number of digits.
There are three modules of genetic operators.
First one is [basic](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/utils/operators/basic.py). It containts mutation(), inverse() and crossover operators.
Second one is [modified](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/utils/operators/modified.py). Its basic operators which are modified in some ways.
Third one is [new](https://github.com/GeorgeFucker/Genetic-Algorithms/blob/master/src/utils/operators/new.py). These operators are not modified version of basic ones. They are standalone operators.
All operators except crossover ones should be passed as mutator argument to the model and crossover ones as crossover argument.

In the future I would like to add more models and more genetic operators which can support more than two parents for crossover operator and spawn more than two children for example.
Also scalability of functions should be added because it helps to avoid local optimums better. 
And the last part that I will add is genetic operators which could operate with float numbers. This operators takes float representation of values and modify it in some ways where my genetic operators works just with binary representations.

I was inspired by series of articles [here](https://neuronus.com/theory/em/). This articles are written on Russian.


