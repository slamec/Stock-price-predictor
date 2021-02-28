import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import sys

pd.set_option('display.max_rows', None) #show all the rows "None" is no limit

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2020, 12, 31)

stock_data = web.DataReader("AAPL", 'yahoo', start, end) #possible to use google etc and other e.g. eurostat
stock_data.tail()

with open('filename1.csv', 'w') as f:
    print(stock_data, file=f) #saves to a file
    