from fastapi import FastAPI
from typing import Union
from pilot_detector import main
import sqlite3

app = FastAPI(title="drone API")

@app.get("/")
def get_drones():
    # connect to violators.db and display and return all entries except time
    conn = sqlite3.connect('violators.db')
    c = conn.cursor()
    c.execute("SELECT name, email, phone, x, y FROM violators")
    rows = c.fetchall()
    conn.close()
    return rows
