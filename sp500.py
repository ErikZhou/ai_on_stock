# https://www.toptal.com/machine-learning/s-p-500-automated-trading
from __future__ import division
import graphlab as gl
from datetime import datetime
from yahoo_finance import Share
import urllib2

# download historical prices of S&P 500 index
print('before download')
today = datetime.strftime(datetime.today(), "%Y-%m-%d")
print('after download')
try:
    stock = Share('^GSPC') # ^GSPC is the Yahoo finance symbol to refer S&P 500 index
    print('Share')
# we gather historical quotes from 2001-01-01 up to today
    hist_quotes = stock.get_historical('2011-01-01', today)
# here is how a row looks like
    hist_quotes[0]
    {'Adj_Close': '2091.580078',
    'Close': '2091.580078',
    'Date': '2016-04-22',
    'High': '2094.320068',
    'Low': '2081.199951',
    'Open': '2091.48999',
    'Symbol': '%5eGSPC',
    'Volume': '3790580000'}
except urllib2.URLError, err:
    print err
