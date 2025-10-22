import io
import pytest # imports pytest testing framework used to run and organize tests
from unittest.mock import patch # imports patch -  a decorator that temporarily replaces (mocks) oobjects during testing. Used to fake external dependencies
from finpulse.agents.data_fetcher import DataFetcherAgent # imports actuall class to be tested
import pandas as pd # imports pandas for creating and working with data frames 
import os #imports os for file system operations

# Mock data for yfinance.download
MOCK_DATA = pd.DataFrame({
    'Close': [100.0, 101.0, 102.0],
}, index=pd.date_range(start="2025-10-20", periods=3, freq='D'))
# Logic : Creates a fake stock data to return instead of calling the real yfinance API

# Decorator that mocks the yfinance.download function
# replaces the real yfinance APU call with a fake one
# prevents actual network calls during testing
# mock object passed as mock_download parameter to the test function
@patch('yfinance.download')
def test_fetch_stock_data_success(mock_download):
    # Configuring mock to return mock data
    mock_download.return_value = MOCK_DATA
    agent = DataFetcherAgent()
    data = agent.fetch_stock_data("TEST", "1d", 5, "data/raw/test.csv")
    
    # Assertions
    assert isinstance(data, pd.DataFrame)
    assert 'Close' in data.columns
    assert not data.empty
    assert os.path.exists("data/raw/test.csv")
    mock_download.assert_called_once_with("TEST", period="5d", interval="1d", auto_adjust=False, progress=False)

@patch('yfinance.download')
def test_fetch_stock_data_empty(mock_download, capfd):
    mock_download.return_value = pd.DataFrame()
    agent = DataFetcherAgent()
    data = agent.fetch_stock_data("TEST", "id", 5, "data/raw/test_empty.csv")
    
    #Assertions
    assert isinstance(data, pd.DataFrame)
    assert data.empty
    out, _ = capfd.readouterr()
    assert "Error fetching data for TEST" in out
    assert not os.path.exists("data/raw/test_empty.csv")

def test_run_with_config():
    agent = DataFetcherAgent()
    with patch('builtins.open', return_value=io.StringIO(""" 
                                                        tickers:
                                                            - TEST
                                                        timeframe: "1d"
                                                        range: 5
                                                        data_dir: "data/raw"
                                                        """)) as mock_file:
        with patch('finpulse.agents.data_fetcher.DataFetcherAgent.fetch_stock_data', return_value=MOCK_DATA):
            results = agent.run()
    
    #Assertions
    assert isinstance(results, dict)
    assert "TEST" in results
    assert isinstance(results["TEST"], pd.DataFrame)
    assert not results["TEST"].empty