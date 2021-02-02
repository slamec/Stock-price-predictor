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
style.use('ggplot')


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2020, 12, 31)

stock_data = web.DataReader("AAPL", 'yahoo', start, end) #possible to use google etc and other e.g. eurostat
stock_data.tail()

close_px = stock_data['Adj Close'] #get the close_px
moving_avarage = close_px.rolling(window=100).mean() #rolling the close_px
moving_avarage


