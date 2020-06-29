import random
import statistics 
import matplotlib.pyplot as plt

PopData = list()

random.seed(5)

for i in range(100):
    DataElem = 10 * random.random()
    PopData.append(DataElem)
    

def CVCalc(Dat):
    CVCalc = statistics.stdev(Dat)/statistics.mean(Dat) 
    return CVCalc

CVPopData = CVCalc(PopData)
print(CVPopData)

N = len(PopData)
JackVal = list()
PseudoVal = list()
for i in range(N-1):
    JackVal.append(0)
for i in range(N):
    PseudoVal.append(0)

for i in range(N):
    for j in range(N):
        if(j < i): 
            JackVal[j] = PopData[j]
        else:
            if(j > i):
                JackVal[j-1]= PopData[j]
    PseudoVal[i] = N*CVCalc(PopData)-(N-1)*CVCalc(JackVal)
    
plt.hist(PseudoVal)
plt.show()

MeanPseudoVal=statistics.mean(PseudoVal)
print(MeanPseudoVal)
VariancePseudoVal=statistics.variance(PseudoVal)
print(VariancePseudoVal)
VarJack = statistics.variance(PseudoVal)/N
print(VarJack)

    