import random
import numpy as np 
import matplotlib.pyplot as plt

PopData = list()

random.seed(7)

for i in range(1000):
    DataElem = 50 * random.random()
    PopData.append(DataElem)
    

PopSample = random.choices(PopData, k=100)

PopSampleMean = list()
for i in range(10000):  
    SampleI = random.choices(PopData, k=100)
    PopSampleMean.append(np.mean(SampleI))

plt.hist(PopSampleMean)
plt.show()

MeanPopSampleMean = np.mean(PopSampleMean)
print("The mean of the Bootstrap estimator is ",MeanPopSampleMean)

MeanPopData = np.mean(PopData)
print("The mean of the population is ",MeanPopData)

MeanPopSample = np.mean(PopSample)
print("The mean of the simple random sample is ",MeanPopSample)

