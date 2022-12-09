import config
import sqlite3
from alpaca.trading.client import TradingClient 

def populate_stocks():
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT symbol,name FROM stock")
    rows = cursor.fetchall()
    symbols=[row['symbol'] for row in rows]
    # api=tradeapi.REST(config.API_KEY,config.SECRET_KEY,base_url=config.API_URL)
    api=TradingClient(config.API_KEY,config.SECRET_KEY,paper=True,url_override=config.API_URL)
    assets=api.get_all_assets()
    # print(assets)
    # print(len(assets))

    # 'asset_class': <AssetClass.CRYPTO: 'crypto'>,
    for asset in assets:
        try:
            if asset.status=="active" and asset.tradable and asset.asset_class != "crypto" and asset.symbol not in symbols:
                print(f"Added a new stock {asset.symbol} {asset.name} {asset.asset_class}")
                cursor.execute("INSERT INTO stock (symbol,name) VALUES (?,?)",(asset.symbol,asset.name))
        except Exception as e:
            print(asset.symbol)
            print(e)
    
    connection.commit()
    
    
if __name__=="__main__":
    populate_stocks()
    pass
