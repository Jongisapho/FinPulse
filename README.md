# FinPulse
## FinPulse is an agent that uses real-time stock data to analyze trends, predict short-term prices and generates reports with visualisations for proactive insights.

*  Python 3.13 - runtime environment and supporting libraries for data processing, analysis and visualization
* Poetry - Dependency management and packaging tool , Facilitates virtual environment and deployment configuration
* yfinance - for fetching real-time and historical market data
* pandas - for Data manipulation to handle DataFrames and multi-index handling
* numpy - Numerical computing library, supports ta-lib to convert pandas series to NumPy 
* ta-lib - Technical analysis library for generating and saving visulizations of market prices
* pyyaml - Used for parsing to read configs for ticker information
* python-dotenv.- Used for environment variable management ( Security )
* Actions - automating builds, dependency installations and script execution
* pytest - N/A
* tensorflow - N/A
* prophet - N/A
* argparse
* Cloud-Platform

<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" fill="none" viewBox="0 0 256 256"><rect width="256" height="256" fill="#242938" rx="60"/><path fill="#2489CA" d="M33.7158 100.208C33.7158 100.208 28.9814 96.795 34.6627 92.2381L47.8994 80.402C47.8994 80.402 51.6869 76.4172 55.6915 79.8891L177.84 172.368V216.714C177.84 216.714 177.781 223.678 168.844 222.908L33.7158 100.208Z"/><path fill="#1070B3" d="M65.1997 128.792L33.7157 157.415C33.7157 157.415 30.4805 159.822 33.7157 164.123L48.3333 177.418C48.3333 177.418 51.8052 181.147 56.9341 176.905L90.3119 151.596L65.1997 128.792Z"/><path fill="#0877B9" d="M120.474 129.029L178.215 84.9391L177.84 40.83C177.84 40.83 175.374 31.2033 167.148 36.2139L90.312 106.145L120.474 129.029Z"/><path fill="#3C99D4" d="M168.844 222.968C172.198 226.4 176.262 225.276 176.262 225.276L221.259 203.103C227.019 199.177 226.21 194.305 226.21 194.305V61.8982C226.21 56.0788 220.252 54.0667 220.252 54.0667L181.253 35.267C172.731 30 167.148 36.2139 167.148 36.2139C167.148 36.2139 174.328 31.0455 177.84 40.83V215.905C177.84 217.109 177.583 218.292 177.071 219.358C176.045 221.429 173.816 223.362 168.47 222.553L168.844 222.968Z"/></svg>

## How to Setup and Run the system
1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run: `poetry run python src/finpulse/main.py`

## Status
Done : Data fetching and basic agent setup <br>
In Progress : Unit test for DataFetcherAgent <br> 
To-DO : predictive modelling with tensorflow and prophet <br>
To-DO : command-line interface for timeframe and range selection <br>
To-DO : Deploy the application <br>
