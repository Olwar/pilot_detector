#!/bin/bash

# This script is used to launch the application locally

# install all the depencies
pip install -r requirements.txt

# run the backend
cd backend
python3 pilot_detector.py > /dev/null &
uvicorn main:app --reload > /dev/null &

# run the frontend
cd ../frontend
echo "Press that ip-address to see the website"
python -m http.server 1337
