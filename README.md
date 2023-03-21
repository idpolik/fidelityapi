# fidelityapi
Python mini-library for interfacing with the undocumented Fidelity FastQuote API

# Usage:
```python
from fidelityapi import *
symbol = "AAPL"
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 10)

api = FidelityAPI(symbol, start_date, end_date)

print(api.get_bar_record())
```
# Features

Create a FidelityAPI object :
```python
fidelity = FidelityAPI(symbol, start_date, end_date)
```

Get a dictionary of Bar Records :
```python
bar_records = fidelity.get_bar_record()
```
Get the day open :
```python
day_open = fidelity.get_day_open()
```
Get the day low :
```python
day_low = fidelity.get_day_low()
```
Get the day high :
```python
day_high = fidelity.get_day_high()
```
Get the percent change :
```python
percent_change = fidelity.get_percent_change()
```
Get the dollar change :
```python
dollar_change = fidelity.get_dollar_change()
```
Get the last price :
```python
last_price = fidelity.get_last_price()
```
Get the last close :
```python
last_close = fidelity.get_last_close()
```
Get the raw response JSON as a dictionary :
```python
raw_data = fidelity.get_data()
```

# Parameters

symbol (required): A string representing the stock symbol.
start_date (required): A datetime object representing the start date of the historical data to retrieve.
end_date (required): A datetime object representing the end date of the historical data to retrieve.
interval (optional): An integer representing the number of minutes in each bar record. Defaults to 5, max 60. Can also be represented as 'WEEKLY', 'DAILY', 'QUARTERLY', 'ANNUAL'
extended_hours (optional): A boolean indicating whether to include extended hours trading data. Defaults to False. 
corp_actions (optional): A boolean indicating whether to include corporate actions data. Defaults to True.
num_days (optional): An integer representing the number of days to retrieve data for. Defaults to 2.
use_cache (optional): A boolean indicating whether to use cached data. Defaults to True.
product_id (optional): A string representing the product ID. Defaults to "oce".
callback (optional): A string representing the callback function name. Defaults to "Fidelity". 
uuid (optional): A string representing the UUID. Defaults to "Fidelity".
timestamp (optional): A string representing the timestamp. Defaults to "start".
quote_type (optional): A string representing the quote type. Defaults to "R".
