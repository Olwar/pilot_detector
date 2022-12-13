#!/bin/bash

# This script is used to launch the application locally

# install all the depencies
sudo apt install python3
pip install -r requirements.txt

# run the backend
cd backend
python3 pilot_detector.py > /dev/null &
uvicorn main:app --reload > /dev/null &
sleep 3

# run the frontend
cd ../frontend
echo "Press that ip-address with port 1337 to see the website"
python3 -m http.server 1337

echo " "
echo "Write kill to kill all the background processes used for this"
echo " "
while :
do
    read var
    if  [ "$var" = "kill" ]
        then
            killall python3 > /dev/null &
            pkill uvicorn > /dev/null &
            break
        fi 
done
