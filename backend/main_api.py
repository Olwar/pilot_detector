from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pilot_detector import main
import sqlite3

app = FastAPI(title="drone API")

# CORS configuration
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# gets all the drone info from the violators database
@app.get("/")
def get_drones():
    conn = sqlite3.connect('violators.db')
    c = conn.cursor()
    c.execute("SELECT id, name, email, phone, x, y FROM violators")
    rows = c.fetchall()
    conn.close()
    return rows

# gets the image with the drones marked
@app.get("/img")
def send_img():
    return FileResponse('birdnest_copy.png')
