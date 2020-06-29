import numpy as np
import matplotlib.pyplot as plt
a=1
b=100
N=100  
X1=np.random.uniform(a,b,N)
plt.plot(X1)
plt.show()
plt.figure()
plt.hist(X1, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

a=1
b=100
N=10000  
X2=np.random.uniform(a,b,N)

plt.figure()
plt.plot(X2)
plt.show()

plt.figure()
plt.hist(X2, density=True, histtype='stepfilled', alpha=0.2)
plt.show()


