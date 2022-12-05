from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pilot_detector import main
import sqlite3
import cv2

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
    conn = sqlite3.connect('violators.db')
    c = conn.cursor()
    c.execute("SELECT id, name, email, phone, x, y FROM violators")
    rows = c.fetchall()
    conn.close()
    return rows

@app.get("/img")
def send_img():
    return FileResponse('birdnest_copy.png')
