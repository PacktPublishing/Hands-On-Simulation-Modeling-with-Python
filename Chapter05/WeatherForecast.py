import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
StatesData = ["Sunny","Rainy"]

TransitionStates = [["SuSu","SuRa"],["RaRa","RaSu"]]
TransitionMatrix = [[0.80,0.20],[0.25,0.75]]


WeatherForecasting = list()
NumDays = 365
TodayPrediction = StatesData[0]

print("Weather initial condition =",TodayPrediction)


for i in range(1, NumDays):
    
    if TodayPrediction == "Sunny":        
        TransCondition = np.random.choice(TransitionStates[0],replace=True,p=TransitionMatrix[0])
        if TransCondition == "SuSu":
            pass
        else:
            TodayPrediction = "Rainy"


            
    elif TodayPrediction == "Rainy":
        TransCondition = np.random.choice(TransitionStates[1],replace=True,p=TransitionMatrix[1])
        if TransCondition == "RaRa":
            pass
        else:
            TodayPrediction = "Sunny"

            
    WeatherForecasting.append(TodayPrediction) 
    print(TodayPrediction)


plt.plot(WeatherForecasting)
plt.show()

plt.figure()
plt.hist(WeatherForecasting)
plt.show()
