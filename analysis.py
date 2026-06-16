import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="3mo")

    df["MA7"] = df["Close"].rolling(window=7).mean()
    df["MA20"] = df["Close"].rolling(window=20).mean()

    signal = "Hold"

    if len(df) >= 20:
        if df["MA7"].iloc[-1] > df["MA20"].iloc[-1]:
            signal = "Buy"
        elif df["MA7"].iloc[-1] < df["MA20"].iloc[-1]:
            signal = "Sell"

    return df, signal
