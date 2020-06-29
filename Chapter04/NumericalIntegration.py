import random 
import numpy as np
import matplotlib.pyplot as plt

random.seed(2)
f = lambda x: x**2
a = 0.0

b = 3.0
NumSteps = 1000000 
XIntegral=[]  
YIntegral=[]
XRectangle=[]  
YRectangle=[]

ymin = f(a)
ymax = ymin
for i in range(NumSteps):
    x = a + (b - a) * float(i) / NumSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y

A = (b - a) * (ymax - ymin)
N = 1000000 
M = 0
for k in range(N):
    x = a + (b - a) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if y <= f(x):
            M += 1 
            XIntegral.append(x)
            YIntegral.append(y)  
    else:
            XRectangle.append(x) 
            YRectangle.append(y)              
NumericalIntegral = M / N * A
print ("Numerical integration = " + str(NumericalIntegral))

XLin=np.linspace(a,b)
YLin=[]
for x in XLin:
    YLin.append(f(x))

plt.axis   ([0, b, 0, f(b)])                                            
plt.plot   (XLin,YLin, color="red" , linewidth="4") 
plt.scatter(XIntegral, YIntegral, color="blue", marker   =".") 
plt.scatter(XRectangle, YRectangle, color="yellow", marker   =".")
plt.title  ("Numerical Integration using Monte Carlo method")
plt.show()
