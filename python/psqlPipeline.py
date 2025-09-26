import pandas as pd
import features
import os

def pipeline():
    # Pull in csv
    filename = 'AAPL.csv'
    path = os.path.join('data', 'AAPL.csv')
    print(path)
    df = pd.read_csv(path)

    features.SMA(df, 10)
    features.EMA(df, 10)
    features.pctChange(df)
    features.volatility(df, 10)

    print(df.head())

pipeline()
    