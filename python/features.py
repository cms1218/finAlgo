import pandas as pd
import os

filename = 'AAPL.csv'
data = pd.read_csv(os.path.join('data', filename))

# Generate Simple moving average column
def SMA(df : pd.DataFrame, length=20):
    df[("SMA" + str(length))] = df['Close'].rolling(length).mean()

# Generate Returns column
def pctChange(df : pd.DataFrame):
    df['Returns'] = df['Close'].pct_change()

# Generate Exponential Moving Average column
def EMA(df : pd.DataFrame, length=21):
    df[("EMA" + str(length))] = df['Close'].ewm(span=length, adjust=False).mean()

# Generate volatility column
def volatility(df : pd.DataFrame, length=10):
    df[('Volatility')] = df['Returns'].rolling(length).std()