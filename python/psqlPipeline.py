import pandas as pd
import features
import os

def pipeline():
    # Pull in csv
    filename = 'AAPL.csv'
    path = os.path.join('data', 'AAPL.csv')
    df = pd.read_csv(path)

    # The methods used to store the Yfinance data to CSV produce two stray rows at the top of the csv. This removes those rows.
    df.drop([0,1],inplace=True)

    # Check for and handle missing values
    if df.isnull().sum().sum() != 0:
        print("Missing Values Detected. Please try reloading the data. ")
        exit(0)

    # Ensure certain columns are numeric
    df['Close'] = pd.to_numeric(df['Close'])
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])
    df['Open'] = pd.to_numeric(df['Open'])
    df['Volume'] = pd.to_numeric(df['Volume'])

    # Add new columns to the dataframe of popular financial indicators
    features.SMA(df, 10)
    features.EMA(df, 10)
    features.pctChange(df)
    features.volatility(df, 10)

    print(df["Close"].dtype)
    print(df.tail())

    

pipeline()
    