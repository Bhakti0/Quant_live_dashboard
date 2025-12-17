
import sqlite3

def init_db():
    conn = sqlite3.connect("ticks.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS ticks (
            timestamp REAL,
            symbol TEXT,
            price REAL,
            qty REAL
        )
    """)
    conn.commit()
    return conn
