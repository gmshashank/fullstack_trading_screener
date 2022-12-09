import config
import sqlite3

from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient    # Create stock historical data client

# # Data by minute
# # client = StockHistoricalDataClient(api_key, api_secret)
# client=StockHistoricalDataClient(config.API_KEY,config.SECRET_KEY)    
# request_params = StockBarsRequest(
#                         symbol_or_symbols=["AAPL", "TSLA"],
#                         timeframe=TimeFrame.Day,
#                         start="2022-10-04 00:00:00",
#                         # end="2022-10-06 00:00:00"
#                  )
# bars = client.get_stock_bars(request_params)
# bars_df = bars.df
# print(bars_df)

def populate_price():
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT id,symbol,name FROM stock")
    rows = cursor.fetchall()
    symbols = [row['symbol'] for row in rows]
    # print(symbols)
    stock_dict={}
    for row in rows:
        symbol=row["symbol"]
        symbols.append(symbol)
        stock_dict[symbol]=row["id"]

    client=StockHistoricalDataClient(config.API_KEY,config.SECRET_KEY)    
    chunk_size=200
    # for i in range(0,len(symbols),chunk_size):
    for i in range(0,1,chunk_size):
        symbol_chunk=symbols[i:i+chunk_size]
        print(symbol_chunk)
        # print(type(symbol_chunk))
        request_params=StockBarsRequest(
            symbol_or_symbols=symbol_chunk,
            timeframe=TimeFrame.Day
            # ,start="2010-10-04 00:00:00",
            )
        # barsets=client.get_stock_bars()
        barsets=client.get_stock_bars(request_params)
        # print(barsets)
        # # print(type(barsets))
        # barsets_df=barsets.df
        # # print(barsets_df.head())
        # print(barsets_df)
        # print(barsets_df.columns)


        for key,val in barsets:
            print(key)
            print(val)
            print(type(val))
            print(val.keys())
            print(val.values())
            for dict_key in val.values():
                print(f"dict_key: {dict_key}")
                print(type(dict_key))
                print(type(dict_key[0]))
            # print(type(val.values()))
            # print((val.values())["open"])

    #     for symbol in barsets:
    #         print(f"Processing symbol:- {symbol}")
    #         # print(type(symbol))
    #         print(f" barsets[symbol]: {barsets[symbol]}")
    #         # print(f" barsets[symbol]: {(symbol[1].values())}")
    #         for bar in barsets[symbol]:
    #             print(bar)
    #         #     stock_id=stock_dict[symbol]
    #         #     cursor.execute("INSERT INTO stock_price (stock_id,date,open,high,low,close,volume) VALUES (?,?,?,?,?,?,?)",(stock_id,bar.t.date(),bar.o,bar.h,bar.l,bar.c,bar.v))
    
    # connection.commit()
    # pass

if __name__ == "__main__":
    populate_price()
    pass