import datetime as dt
import numpy as np
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

StockList = ['ADBE','CSCO','IBM','NVDA','MSFT','HPQ'] 
StartDay = dt.datetime(2019, 1, 1)
EndDay = dt.datetime(2019, 12, 31)

StockData =  wb.DataReader(StockList, 'yahoo',StartDay,EndDay)
StockClose = StockData["Adj Close"]
print(StockClose.describe())

fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(StockClose['ADBE'])
axs[0, 0].set_title('ADBE')
axs[0, 1].plot(StockClose['CSCO'])
axs[0, 1].set_title('CSCO')
axs[1, 0].plot(StockClose['IBM'])
axs[1, 0].set_title('IBM')
axs[1, 1].plot(StockClose['NVDA'])
axs[1, 1].set_title('NVDA')
axs[2, 0].plot(StockClose['MSFT'])
axs[2, 0].set_title('MSFT')
axs[2, 1].plot(StockClose['HPQ'])
axs[2, 1].set_title('HPQ')

plt.figure(figsize=(10,5))
plt.plot(StockClose)
plt.show()

StockReturns = StockClose.pct_change()
print(StockReturns.tail(15))

PortvolioValue = 1000000000.00
ConfidenceValue = 0.95
MeanStockRet = np.mean(StockReturns)
StdStockRet = np.std(StockReturns)

WorkingDays2019 = 252.
AnnualizedMeanStockRet = MeanStockRet/WorkingDays2019
AnnualizedStdStockRet = StdStockRet/np.sqrt(WorkingDays2019)

INPD = norm.ppf(1-ConfidenceValue,AnnualizedMeanStockRet,AnnualizedStdStockRet)
VaR = PortvolioValue*INPD

RoundVaR=np.round_(VaR,2)

for i in range(len(StockList)):
    print("Value-at-Risk for", StockList[i], "is equal to ",RoundVaR[i])
