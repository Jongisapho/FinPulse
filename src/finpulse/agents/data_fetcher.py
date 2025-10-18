import yfinance as yf
import pandas as pd
import os
import yaml
from dotenv import load_dotenv

load_dotenv()

class DataFetcherAgent:
    def __init__(self):
        self.role = "Data Fetcher"
        self.goal = "Fetch historical and real-time stock data for given tickers"

    def fetch_stock_data(self, ticker: str, timeframe: str, periods: int, save_path: str) -> pd.DataFrame:
        """Fetch stock data and save to CSV."""
        try:
            data = yf.download(ticker, period=f"{periods}d", interval=timeframe, auto_adjust=False, progress=False)
            if data.empty:
                raise ValueError(f"No data found for {ticker}")
            # Flatten multi-index if present
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            data.to_csv(save_path)
            return data
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return pd.DataFrame()

    def run(self, config_path: str = "config/config.yaml") -> dict:
        """Run agent to fetch data for all tickers in config."""
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        tickers = config.get("tickers", [])
        timeframe = config.get("timeframe", "1d")
        periods = config.get("range", 252)
        data_dir = config.get("data_dir", "data/raw")
        
        results = {}
        for ticker in tickers:
            save_path = os.path.join(data_dir, f"{ticker}_{timeframe}.csv")
            data = self.fetch_stock_data(ticker, timeframe, periods, save_path)
            results[ticker] = data
        return results