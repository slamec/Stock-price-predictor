import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import sys


import matplotlib.pyplot as plt #importing matplotlib 
import matplotlib as mpl
from matplotlib import style

pd.set_option('display.max_rows', None) #show all the rows "None" is no limit
plt.rcParams["figure.figsize"] = (8,7) #adjusting size of matblotlib
style.use('ggplot') #adjusting the style, possible to use different styles


start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2021, 1, 31)

stock_data = web.DataReader(['AAPL', 'MSFT', 'GOOGL', 'AMZN'], 'yahoo', start, end)['Adj Close'] #possible to use google etc and other e.g. eurostat
#Adj close to show more tickers
stock_data.shape

#getting the percantage change
rets = stock_data.pct_change()
#+ correlation from the percantage change
corr = rets.corr()
corr

#creating a scatterplot
plt.scatter(rets.AAPL, rets.MSFT)
plt.xlabel("AAPL")
plt.ylabel("MSFT")




