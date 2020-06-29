import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def matyas(x):
   return 0.26*(x[0]**2+x[1]**2)-0.48*x[0]*x[1]

#def booth(x):
#   return (x[0]+2*x[1]-7)**2+(2*x[0]+x[1]-5)**2

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
x, y = np.meshgrid(x, y)
z = matyas([x,y])

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()



x0 = np.array([-10, 10])
NelderMeadOptimizeResults = minimize(matyas, x0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})

print(NelderMeadOptimizeResults.x)




x0 = np.array([-10, 10])
PowellOptimizeResults = minimize(matyas, x0, method='Powell',
               options={'xtol': 1e-8, 'disp': True})

print(PowellOptimizeResults.x)