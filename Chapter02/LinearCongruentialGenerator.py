import numpy as np
a = 2
c = 4
m = 5
x  = 3

for i in range(1,17):
    x= np.mod((a*x+c),m)
    print(x)