import config

# from alpaca.data.historical import StockHistoricalDataClient
# from alpaca.data.requests import StockLatestQuoteRequest
# from alpaca.data.timeframe import TimeFrame

# # keys required for stock historical data client
# client = StockHistoricalDataClient(config.API_KEY, config.SECRET_KEY)

# # multi symbol request - single symbol is similar
# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

# latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)
# client.get_stock_bars()

# gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price
# print(gld_latest_ask_price)


from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient# Create stock historical data client
# keys required for stock historical data client
client = StockHistoricalDataClient(config.API_KEY, config.SECRET_KEY)
request_params = StockBarsRequest(
                        symbol_or_symbols=["TSLA"],
                        timeframe=TimeFrame.Day,
                        start="2022-01-01 00:00:00"
                 )
bars = client.get_stock_bars(request_params)
bars_df = bars.df
print(bars_df)


# import datetime as dt
# import pytz
# def get_last2Days_bars(_ticker):
#     _timeNow = dt.datetime.now(pytz.timezone('US/Eastern'))
#     _2DaysAgo = _timeNow - dt.timedelta(days=2) 

#     _bars = api.get_bars(_ticker, TimeFrame.Day,
#                          start=_2DaysAgo.isoformat(),
#                          end=None,
#                          limit=2
#                          )
#     print(_bars)


# # Crypto
# from alpaca.data.historical import CryptoHistoricalDataClient
# from alpaca.data.requests import CryptoBarsRequest
# from alpaca.data.timeframe import TimeFrame

# # no keys required for crypto data
# client = CryptoHistoricalDataClient()

# request_params = CryptoBarsRequest(
#                         symbol_or_symbols=["BTC/USD", "ETH/USD"],
#                         timeframe=TimeFrame.Day,
#                         start="2022-09-01T07:20:50.52Z"
#                  )

# bars = client.get_crypto_bars(request_params)

# # convert to dataframe
# bars=bars.df

# # access bars as list - important to note that you must access by symbol key
# # even for a single symbol request - models are agnostic to number of symbols
# print(bars["BTC/USD"])