import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,3,100)
y=x**2-2*x+1

fig = plt.figure()
axdef = fig.add_subplot(1, 1, 1)
axdef.spines['left'].set_position('center')
axdef.spines['bottom'].set_position('zero')
axdef.spines['right'].set_color('none')
axdef.spines['top'].set_color('none')
axdef.xaxis.set_ticks_position('bottom')
axdef.yaxis.set_ticks_position('left')

plt.plot(x,y, 'r')
plt.show()

Gradf = lambda x: 2*x-2  

ActualX = 3 
LearningRate = 0.01 
PrecisionValue = 0.000001 
PreviousStepSize = 1 
MaxIteration = 10000 
IterationCounter = 0 


while PreviousStepSize > PrecisionValue and IterationCounter < MaxIteration:
    PreviousX = ActualX
    ActualX = ActualX - LearningRate * Gradf(PreviousX) 
    PreviousStepSize = abs(ActualX - PreviousX) 
    IterationCounter = IterationCounter+1 
    print("Number of iterations = ",IterationCounter,"\nActual value of x  is = ",ActualX) 
    
print("X value of f(x) minimum = ", ActualX)