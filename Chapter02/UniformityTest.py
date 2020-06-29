import numpy as np
a = 75
c = 0
m = 2**(31) -1
x  = 0.1
u=np.array([])

for i in range(0,100):
    x= np.mod((a*x+c),m)
    u= np.append(u,x/m)
    print(u[i])
    
N=100
s=20
Ns =N/s
S = np.arange(0, 1, 0.05)
counts = np.empty(S.shape, dtype=int)
V=0
for i in range(0,20):
    counts[i] = len(np.where((u >= S[i]) & (u < S[i]+0.05))[0])
    V=V+(counts[i]-Ns)**2 / Ns

print("R = ",counts)
print("V = ", V)

import matplotlib.pyplot as plt
Ypos = np.arange(len(counts))

plt.bar(Ypos,counts)