import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
try:
    import talib
except ImportError:
    talib = None

def calculate_moving_average(data: pd.DataFrame, window: int = 20) -> pd.Series:
    """Calculate simple moving average for stock prices."""
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain 'Close' column")
    return data['Close'].rolling(window=window).mean()

def calculate_rsi(data: pd.DataFrame, period: int = 14) -> pd.Series:
    """Calculate Relative Strength Index."""
    if talib is not None:
        # Ensure Close is a flat Series, handle multi-index
        close = data['Close']
        if isinstance(data.index, pd.MultiIndex):
            close = data['Close'].xs('Close', level=1, axis=1, drop_level=True)
        # Convert to NumPy array, drop NaNs
        close_prices = close.dropna().to_numpy(dtype=np.float64)
        # Check if enough data points for RSI
        if len(close_prices) < period + 1:
            print(f"Warning: Not enough data points ({len(close_prices)}) for RSI period {period}")
            return pd.Series(np.full(len(data), 50.0), index=data.index)
        try:
            return pd.Series(talib.RSI(close_prices, timeperiod=period), index=close.index)
        except Exception as e:
            print(f"ta-lib RSI failed: {e}. Falling back to manual RSI.")
    # Manual RSI calculation
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rs = rs.replace([np.inf, -np.inf], np.nan)
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)  # Fill NaN with neutral RSI value

def add_technical_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """Add technical indicators (SMA, RSI)."""
    data = data.copy()
    data['SMA20'] = calculate_moving_average(data, window=20)
    data['RSI'] = calculate_rsi(data)
    return data

def plot_stock_data(data: pd.DataFrame, ticker: str):
    """Plot closing prices, SMA, and RSI."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ax1.plot(data.index, data['Close'], label='Close Price')
    ax1.plot(data.index, data['SMA20'], label='20-Day SMA', linestyle='--')
    ax1.set_title(f"{ticker} Stock Price")
    ax1.set_ylabel("Price (USD)")
    ax1.legend()
    ax1.grid()

    ax2.plot(data.index, data['RSI'], label='RSI', color='purple')
    ax2.axhline(70, linestyle='--', alpha=0.5, color='red')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='green')
    ax2.set_ylabel("RSI")
    ax2.legend()
    ax2.grid()

    os.makedirs("data/processed", exist_ok=True)
    plt.savefig(f"data/processed/{ticker}_plot.png")
    plt.close()