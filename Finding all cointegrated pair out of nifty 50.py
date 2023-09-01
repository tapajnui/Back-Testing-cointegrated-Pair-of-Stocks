# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y28t8g5BXgDKfZwYFyduP1rGeyUwCcK3
"""

import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import coint
from itertools import combinations

# Get the stock prices for all the stocks in the list
stock_prices = pd.DataFrame()
cnt=0
stocks = ['ADANIENT.NS',
    'ADANIPORTS.NS',
    'APOLLOHOSP.NS',
    'ASIANPAINT.NS',
    'AXISBANK.NS',
    'BAJAJ-AUTO.NS',
    'BAJFINANCE.NS',
    'BAJAJFINSV.NS',
    'BPCL.NS',
    'BHARTIARTL.NS',
    'BRITANNIA.NS',
    'CIPLA.NS',
    'COALINDIA.NS',
    'DIVISLAB.NS',
    'DRREDDY.NS',
    'EICHERMOT.NS',
    'GRASIM.NS',
    'HCLTECH.NS',
    'HDFCBANK.NS',
    'HDFCLIFE.NS',
    'HEROMOTOCO.NS',
    'HINDALCO.NS',
    'HINDUNILVR.NS',
    'ICICIBANK.NS',
    'ITC.NS',
    'INDUSINDBK.NS',
    'INFY.NS',
    'JSWSTEEL.NS',
    'KOTAKBANK.NS',
    'LT.NS',
    'M&M.NS',
    'MARUTI.NS',
    'NTPC.NS',
    'NESTLEIND.NS',
    'ONGC.NS',
    'POWERGRID.NS',
    'RELIANCE.NS',
    'SBILIFE.NS',
    'SBIN.NS',
    'SUNPHARMA.NS',
    'TCS.NS',
    'TATACONSUM.NS',
    'TATAMOTORS.NS',
    'TATASTEEL.NS',
    'TECHM.NS',
    'TITAN.NS',
    'UPL.NS',
    'ULTRACEMCO.NS',
    'WIPRO.NS']

# Fetch stock data using yfinance and add to the DataFrame
for stock in stocks:
    stock_prices[stock] = yf.download(stock, start="1992-01-01", end="2023-01-01")["Close"]

# Check for missing values
missing_values = stock_prices.isnull()

# Delete the rows with missing values
stock_prices = stock_prices.dropna(how="any")

# Calculate the cointegration test for all pairs of stocks
cointegration_results = {}
for stock_1, stock_2 in combinations(stock_prices.columns, 2):
    result = coint(stock_prices[stock_1], stock_prices[stock_2])
    if result[1] < 0.05:  # Check if p-value is less than 0.05
        cointegration_results[(stock_1, stock_2)] = result[1]
        cnt +=1

# Print the results of the cointegration tests
for stock_1, stock_2 in cointegration_results.keys():
    print(f"{stock_1} and {stock_2}")

print("count :", cnt)