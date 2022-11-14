import config
import sqlite3

def create_db():
    connection=sqlite3.connect(config.DB_FILE)

    cursor =connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company TEXT NOT NULL
    )
    """)
    
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS stock_price (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER,
    date NOT NULL,
    open NOT NULL,
    high NOT NULL,
    low NOT NULL,
    close NOT NULL,
    adjusted_close NOT NULL,
    volume NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
    """)

    connection.commit()

if __name__=="__main__":
    create_db()

