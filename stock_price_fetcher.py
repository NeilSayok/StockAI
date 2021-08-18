# Raw Package
import numpy as np
from numpy.core.records import fromrecords
import pandas as pd
from time import sleep

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

def fetch_data(tickers):
    df =  yf.download(tickers=tickers, period='1d', interval='1m')
    #temp = df["Close"][-1]
    #print( f"Close = {temp}")
    print(df)
    #fetch_data(tickers)

#while(True):
fetch_data("TCS.NS BTC-INR")
  