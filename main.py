from fastapi import FastAPI
from typing import Union
from pilot_detector.py import main

app = FastAPI(title="drone API")

@app.get("/")
def get_drones():
    violators_info = main()
    return violators_info
