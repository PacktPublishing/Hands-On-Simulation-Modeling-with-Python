import numpy as np
a = 75
c = 0
m = 2**(31) -1
x  = 0.1

for i in range(1,100):
    x= np.mod((a*x+c),m)
    u = x/m
    print(u)