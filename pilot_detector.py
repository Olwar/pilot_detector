import requests
import xml.etree.ElementTree as ET

# no-fly zone coordinates from (300 000, 300 000) to (200 000, 200 000)

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

def check_drone_position(drones):
    violators = {}
    for drone in drones:
        if float(drones[drone][1]) > 200000 and float(drones[drone][1]) < 300000 and float(drones[drone][2]) > 200000 and float(drones[drone][2]) < 300000:
            violators[drone] = drones[drone]
    return violators

def get_violators_info(violators):
    violators_info = {}
    for k,v in violators.items():
        r = requests.get('http://assignments.reaktor.com/birdnest/pilots/' + v[0])
        data = r.json()
        pilot_name = data['firstName'] + ' ' + data['lastName']
        pilot_email = data['email']
        pilot_phone = data['phoneNumber']
        pos_x, pos_y = v[1], v[2]
        violators_info[k] = [pilot_name, pilot_email, pilot_phone, pos_x, pos_y]
    return(violators_info)

def main():
    drones = get_drone_data()
    violators = check_drone_position(drones)
    violators_info = get_violators_info(violators)
    return violators_info

if __name__ == '__main__':
    main()
