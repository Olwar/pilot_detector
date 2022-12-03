from fastapi import FastAPI
from typing import Union
from pilot_detector import main
import sqlite3

app = FastAPI(title="drone API")

@app.get("/")
def get_drones():
    violators_info = main()
    return violators_info
