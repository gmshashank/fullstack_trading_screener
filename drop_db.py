import config
import sqlite3

def drop_db():
    connection=sqlite3.connect(config.DB_FILE)
    cursor=connection.cursor()
    cursor.execute("DROP TABLE stock_price")
    cursor.execute("DROP TABLE stock")
    connection.commit()

if __name__=="__main__":
    drop_db()