import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import sqlite3
import time
import math

# gets all the drone's positions and serial numbers
def get_drone_data():
    response = requests.get("http://assignments.reaktor.com/birdnest/drones")
    data = response.content
    stuff = ET.fromstring(data)
    tree = stuff.findall('capture/drone')
    i = 0
    drones = {}
    for item in tree:
        serial = item.find('serialNumber').text
        pos_x = item.find('positionX').text
        pos_y = item.find('positionY').text
        drones[f'drone_' + str(i)] = [serial, pos_x, pos_y]
        i += 1
    return drones

# checks if the drones are violating the no-fly zone
def check_drone_position(drones):
    violators = {}
    for drone in drones:
        if float(drones[drone][1]) > 200000 and float(drones[drone][1]) < 300000 and float(drones[drone][2]) > 200000 and float(drones[drone][2]) < 300000:
            violators[drone] = drones[drone]
    return violators

# calculates distance to the nest in meters
def calculate_distance(pos_x, pos_y):
    x_dist = abs(pos_x - 250000) / 1000
    y_dist = abs(pos_y - 250000) / 1000
    return math.sqrt(x_dist**2 + y_dist**2)

# gets violator's name, email, phonenumber and distance to the nest in meters, 250000 equals 0 meters and 0 is 250 meters, 500000 is 500 meters and so on
def get_violators_info(violators):
    violators_info = {}
    for k,v in violators.items():
        r = requests.get('http://assignments.reaktor.com/birdnest/pilots/' + v[0])
        data = r.json()
        pilot_name = data['firstName'] + ' ' + data['lastName']
        pilot_email = data['email']
        pilot_phone = data['phoneNumber']
        pos_x, pos_y = v[1], v[2]
        distance = calculate_distance(float(pos_x), float(pos_y))
        violators_info[k] = [pilot_name, pilot_email, pilot_phone, pos_x, pos_y, distance]
    return(violators_info)

# inserts violator's info to sqlite database and removes all that are older than 10 minutes and if multiple entires from one user, deletes all but the closest one to the one
def database_handler(violators_info):
    conn = sqlite3.connect('violators.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS violators
                 (id integer not null primary key autoincrement, time text, name text, email text, phone text, x text, y text, distance text)''')
    for k,v in violators_info.items():
        c.execute("INSERT INTO violators VALUES (?,?,?,?,?,?,?,?)", (None, datetime.now(), v[0], v[1], v[2], v[3], v[4], v[5]))
    c.execute("DELETE FROM violators WHERE rowid NOT IN (SELECT rowid FROM violators WHERE time > ? GROUP BY name HAVING MIN(ABS(x - 250000) + ABS(y - 250000)))", (datetime.now() - timedelta(minutes=10),))
    conn.commit()
    conn.close()

def main():
    while 1:
        start_time = time.time()
        drones = get_drone_data()
        violators = check_drone_position(drones)
        violators_info = get_violators_info(violators)
        database_handler(violators_info)
        print(f"check completed in {time.time() - start_time} seconds.")
        time.sleep(0.5)

if __name__ == '__main__':
    main()
