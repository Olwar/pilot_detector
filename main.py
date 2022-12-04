from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pilot_detector import main
import sqlite3

app = FastAPI(title="drone API")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_drones():
    # connect to violators.db and display and return all entries except time
    conn = sqlite3.connect('violators.db')
    c = conn.cursor()
    c.execute("SELECT name, email, phone, x, y FROM violators")
    rows = c.fetchall()
    conn.close()
    return rows
