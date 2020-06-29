from random import seed
from random import random
from matplotlib import pyplot
seed(1)
RWPath = list()
RWPath.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
	ZNValue = -1 if random() < 0.5 else 1
	XNValue = RWPath[i-1] + ZNValue
	RWPath.append(XNValue)
pyplot.plot(RWPath)
pyplot.show()