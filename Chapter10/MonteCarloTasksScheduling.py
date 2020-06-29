import pandas as pd
import random
import numpy as np

N = 10000

TotalTime=[]

T =  np.empty(shape=(N,6)) 

TaskTimes=[[3,5,8],
          [2,4,7],
           [3,5,9],
           [4,6,10],
           [3,5,9],
           [2,6,8]]

Lh=[]
for i in range(6):
    Lh.append((TaskTimes[i][1]-TaskTimes[i][0])/(TaskTimes[i][2]-TaskTimes[i][0]))


for p in range(N):
    for i in range(6):
        trand=random.random()
        if (trand < Lh[i]):
            T[p][i] = TaskTimes[i][0] + np.sqrt(trand*(TaskTimes[i][1]-TaskTimes[i][0])*(TaskTimes[i][2]-TaskTimes[i][0]))
        else:
            T[p][i] = TaskTimes[i][2] - np.sqrt((1-trand)*(TaskTimes[i][2]-TaskTimes[i][1])*(TaskTimes[i][2]-TaskTimes[i][0]))
    TotalTime.append( T[p][0]+ np.maximum(T[p][1],T[p][2]) + np.maximum(T[p][3],T[p][4]) + T[p][5])
    
    
Data = pd.DataFrame(T,columns=['Task1', 'Task2', 'Task3', 'Task4', 'Task5', 'Task6'])

pd.set_option('display.max_columns', None)  
print(Data.describe())

hist = Data.hist(bins=10)


print("Minimum project completion time = ",np.amin(TotalTime))

print("Mean project completion time = ",np.mean(TotalTime))

print("Maximum project completion time = ",np.amax(TotalTime))




