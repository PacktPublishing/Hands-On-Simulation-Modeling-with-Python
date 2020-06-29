import pandas as pd

ASNNames= ['Frequency','AngleAttack','ChordLength','FSVelox','SSDT','SSP']

ASNData = pd.read_csv('airfoil_self_noise.dat', delim_whitespace=True, names=ASNNames)

print(ASNData.head(20))

print(ASNData.info())

BasicStats = ASNData.describe()
BasicStats = BasicStats.transpose()
print(BasicStats)


from sklearn.preprocessing import MinMaxScaler

ScalerObject = MinMaxScaler()
print(ScalerObject.fit(ASNData))
ASNDataScaled = ScalerObject.fit_transform(ASNData)
ASNDataScaled = pd.DataFrame(ASNDataScaled, columns=ASNNames)

summary = ASNDataScaled.describe()
summary = summary.transpose()
print(summary)

import matplotlib.pyplot as plt
boxplot = ASNDataScaled.boxplot(column=ASNNames)
plt.show()

CorASNData = ASNDataScaled.corr(method='pearson')
with pd.option_context('display.max_rows', None, 'display.max_columns', CorASNData.shape[1]):
    print(CorASNData)

plt.matshow(CorASNData)
plt.xticks(range(len(CorASNData.columns)), CorASNData.columns)
plt.yticks(range(len(CorASNData.columns)), CorASNData.columns)
plt.colorbar()
plt.show()


from sklearn.model_selection import train_test_split

X = ASNDataScaled.drop('SSP', axis = 1)
print('X shape = ',X.shape)
Y = ASNDataScaled['SSP']
print('Y shape = ',Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.30, random_state = 5)
print('X train shape = ',X_train.shape)
print('X test shape = ', X_test.shape)
print('Y train shape = ', Y_train.shape)
print('Y test shape = ',Y_test.shape)


#Linear Regression
from sklearn.linear_model import LinearRegression

LModel = LinearRegression()
LModel.fit(X_train, Y_train)

Y_predLM = LModel.predict(X_test)

from sklearn.metrics import mean_squared_error

MseLM = mean_squared_error(Y_test, Y_predLM)
print('Linear Regression Model')
print(MseLM)


#MLP Regressor Model
from sklearn.neural_network import MLPRegressor

MLPRegModel = MLPRegressor(hidden_layer_sizes=(50),activation='relu', solver='lbfgs',
                                 tol=1e-4, max_iter=10000, random_state=1)

MLPRegModel.fit(X_train, Y_train)

Y_predMLPReg = MLPRegModel.predict(X_test)

MseMLP = mean_squared_error(Y_test, Y_predMLPReg)
print('SKLearn Neural Network Model')
print(MseMLP)

# Plot a comparison diagram
plt.figure(1)
plt.subplot(121)
plt.scatter(Y_test, Y_predMLPReg)
plt.plot((0, 1), "r--")
plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.title("SKLearn Neural Network Model")

plt.subplot(122)
plt.scatter(Y_test, Y_predLM)
plt.plot((0, 1), "r--")
plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.title("SKLearn Linear Regression Model")
plt.show()





