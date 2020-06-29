import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu = 10
sigma =2

P1 = np.random.normal(mu, sigma, 1000)

mu = 5
sigma =2

P2 = np.random.normal(mu, sigma, 1000)

mu = 15
sigma =2

P3 = np.random.normal(mu, sigma, 1000)

Plot1 = sns.distplot(P1)
Plot2 = sns.distplot(P2)
Plot3 = sns.distplot(P3)


mu = 10
sigma =2

P4 = np.random.normal(mu, sigma, 1000)

mu = 10
sigma =1

P5 = np.random.normal(mu, sigma, 1000)

mu = 10
sigma =0.5

P6 = np.random.normal(mu, sigma, 1000)

plt.figure()
Plot4 = sns.distplot(P4)
Plot5 = sns.distplot(P5)
Plot6 = sns.distplot(P6)
plt.show()




