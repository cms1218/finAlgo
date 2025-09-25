import pandas as pd
import os

filename = 'AAPL.csv'
data = pd.read_csv(os.path.join('data', filename))

def SMA(df : pd.DataFrame, length):
    df[("SMA" + str(length))] = df['Close'].rolling(length).mean()

def pctChange(df : pd.DataFrame):
    df['Returns'] = df['Close'].pct_change()

def EMA(df : pd.DataFrame, length):
    df[("EMA" + str(length))] = df['Close'].ewm(span=length, adjust=False).mean()

def volatility(df : pd.DataFrame, length):
    df[('Volatility')] = df['Returns'].rolling(length).std()