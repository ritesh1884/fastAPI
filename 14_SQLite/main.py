import _sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = _sqlite3.connect("test.db", check_same_thread=False)
# db will be stored in test.db file

cursor = conn.cursor()

# creating a table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
)
""")

conn.commit()

@app.get("/")
def home():
    return {
        "message": "SQLite connected"
    }