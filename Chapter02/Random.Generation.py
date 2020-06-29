import random

for i in range(20):
    print('%05.4f' % random.random(), end=' ')
print()

random.seed(1)

for i in range(20):
    print('%05.4f' % random.random(), end=' ')
print()

for i in range(20):
    print('%6.4f' %random.uniform(1, 100), end=' ')
print()


for i in range(20):
    print(random.randint(-100, 100), end=' ')
print()

for i in range(20):
    print(random.randrange(0, 100,5), end=' ')
print()

CitiesList = ['Rome','New York','London','Berlin','Moskov', 'Los Angeles','Paris','Madrid','Tokio','Toronto']
for i in range(10):
    CitiesItem = random.choice(CitiesList)
    print ("Randomly selected item from Cities list is - ", CitiesItem)
    
DataList = range(10,100,10)
print("Initial Data List = ",DataList)
DataSample = random.sample(DataList,k=5)
print("Sample Data List = ",DataSample)