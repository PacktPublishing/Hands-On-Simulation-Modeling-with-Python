import numpy as np
from sklearn.model_selection import KFold

StartedData=np.arange(10,110,10)
print(StartedData)


kfold = KFold(5, True, 1)

for TrainData, TestData in kfold.split(StartedData):
	print("Train Data :", StartedData[TrainData],"Test Data :", StartedData[TestData])
    
