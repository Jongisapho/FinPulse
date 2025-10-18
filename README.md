# FinPulse
## FinPulse is an agent that uses real-time stock data to analyze trends, predict short-term prices and generates reports with visualisations for proactive insights.

* Poetry used for project structure and dependency management
* Data fetched from yfinance

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
