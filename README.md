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

.g., gh for GitHub,

## How to Setup and Run the system
1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run: `poetry run python src/finpulse/main.py`

## Status
![Codecov](https://codecov.io/gh/jongisapho/finpulse/branch/main/graph/badge.svg)
Done : Data fetching and basic agent setup <br>
In Progress : Unit test for DataFetcherAgent <br> 
To-DO : predictive modelling with tensorflow and prophet <br>
To-DO : command-line interface for timeframe and range selection <br>
To-DO : Deploy the application <br>
