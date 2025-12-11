import sqlite3
from fastapi import FastAPI

app = FastAPI()

DB_NAME = "test.db"

# Create table once when app starts
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn newdpost:app --reload

Ctrl + C to stop the server
"""