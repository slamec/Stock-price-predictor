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


stock_data = web.DataReader('AAPL', 'yahoo', start, end) #possible to use google etc and other e.g. eurostat
stock_data.tail()

close_px = stock_data['Adj Close'] #get the close_px
moving_avarage = close_px.rolling(window=100).mean() #rolling the close_px
moving_avarage


#getting return as a close px in %
rets = close_px.pct_change()
rets.plot(label = 'return') #plot and label it as return


