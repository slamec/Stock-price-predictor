import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import sys

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 12, 31)

stock_data = web.DataReader("AAPL", 'yahoo', start, end)
stock_data.tail()

with open('filename.csv', 'w') as f:
    print(stock_data, file=f)