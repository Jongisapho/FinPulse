from finpulse.agents.data_fetcher import DataFetcherAgent
from finpulse.utils.data_utils import add_technical_indicators, plot_stock_data
import pandas as pd

def main():
       print("Starting FinPulse...")
       fetcher = DataFetcherAgent()
       results = fetcher.run()
       
       for ticker, data in results.items():
           if not data.empty:
               print(f"\nData for {ticker}:")
               data = add_technical_indicators(data)
               print(data[['Close', 'SMA20', 'RSI']].tail())
               plot_stock_data(data, ticker)
               print(f"Plot saved for {ticker} at data/processed/{ticker}_plot.png")
           else:
               print(f"No data retrieved for {ticker}")

if __name__ == "__main__":
    main()