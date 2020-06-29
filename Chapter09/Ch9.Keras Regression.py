import pandas as pd

ASNNames= ['Frequency','AngleAttack','ChordLength','FSVelox','SSDT','SSP']

ASNData = pd.read_csv('airfoil_self_noise.dat', delim_whitespace=True, names=ASNNames)

print(ASNData.head(20))

print(ASNData.info())

summary = ASNData.describe()
summary = summary.transpose()
print(summary)



from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
print(scaler.fit(ASNData))
ASNDataScaled = scaler.fit_transform(ASNData)
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


#MLP Regressor Model
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

MLPRegModel = make_pipeline(StandardScaler(),
                    MLPRegressor(hidden_layer_sizes=(100, 100),
                                 tol=1e-5, max_iter=1000, random_state=0))

MLPRegModel.fit(X_train, Y_train)

Y_predMLPReg = MLPRegModel.predict(X_test)

print('SKLearn Neural Network Model')
print(MLPRegModel.score(X_test, Y_test))

from sklearn.metrics import mean_squared_error

MseMLP = mean_squared_error(Y_test, Y_predMLPReg)
print('SKLearn Neural Network Model')
print(MseMLP)

#Keras Model

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(20, input_dim=5, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=1000, verbose=1)

model.summary()

Y_predKM = model.predict(X_test)

score = model.evaluate(X_test, Y_test, verbose=0)

print('Keras Model')
print(score[0])




plt.figure(1)
plt.subplot(121)
plt.scatter(Y_test, Y_predMLPReg)
plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.title("SKLearn Neural Network Model")

plt.subplot(122)
plt.scatter(Y_test, Y_predLM)
plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.title("SKLearn Linear Regression Model")
plt.show()


MseLM = mean_squared_error(Y_test, Y_predLM)
print('Linear Regression Model')
print(MseLM)


