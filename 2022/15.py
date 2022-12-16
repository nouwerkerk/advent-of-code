import itertools

def calculate_radius(sensor, beacon):
    distanceX = abs(sensor[0] - beacon[0])
    distanceY = abs(sensor[1] - beacon[1])
    return distanceX + distanceY
    
with open('real-input/15.txt', 'r') as file:
    lines = [l for l in file.read().splitlines()]
file.close()

beacons = set()
sensors = set()
sensorBeaconCombos = []

for line in lines:
    coordinates = line.split(': ')
    coorTextSensor = coordinates[0].replace('Sensor at ', '').split(', ')
    coorTextBeacon = coordinates[1].replace('closest beacon is at ', '').split(', ')
    
    coordinatesSensor = (int(coorTextSensor[0].replace('x=', '')), int(coorTextSensor[1].replace('y=', '')))
    coordinatesBeacon = (int(coorTextBeacon[0].replace('x=', '')), int(coorTextBeacon[1].replace('y=', '')))
    beacons.add(coordinatesBeacon)
    sensors.add(coordinatesSensor)
    sensorBeaconCombos.append((coordinatesSensor, coordinatesBeacon))

def part1():
    occupied = set()
    
    for sensorBeacon in sensorBeaconCombos:
        sensor = sensorBeacon[0]
        beacon = sensorBeacon[1]
        radius = calculate_radius(sensor, beacon)

        if ((sensor[1] <= 2000000 and sensor[1] + radius >= 2000000) or (sensor[1] >= 2000000 and sensor[1] - radius <= 2000000)):
            for x in range(sensor[0] - radius, sensor[0] + radius + 1):
                candidate = (x, 2000000)
                if (abs(sensor[0] - x) + abs(sensor[1] - 2000000)) <= radius and candidate not in beacons and candidate not in sensors:
                    occupied.add(candidate)
    return len(occupied)

def part2():
    for sensorBeacon in [x for x in itertools.combinations(sensorBeaconCombos, 2)]:
        visited = set()
        
        sensor1 = sensorBeacon[0][0]
        beacon1 = sensorBeacon[0][1]
        sensor2 = sensorBeacon[1][0]
        beacon2 = sensorBeacon[1][1]
        radius1 = calculate_radius(sensor1, beacon1)
        radius2 = calculate_radius(sensor2, beacon2)
        
        #print(f'new combo: {sensor1} - {sensor2}')
        
        if radius1 + radius2 + 2 == calculate_radius(sensor1, sensor2):
            cornerCoord = set()
            for i in range(0, radius1 + 2):
                cornerCoord.add((sensor1[0] + i, sensor1[1] + (radius1 + 1) - i))
                cornerCoord.add((sensor1[0] + i, sensor1[1] - ((radius1 + 1) - i)))
                cornerCoord.add((sensor1[0] - i, sensor1[1] + (radius1 + 1) - i))
                cornerCoord.add((sensor1[0] - i, sensor1[1] - ((radius1 + 1) - i)))
                
            for coord in cornerCoord:
                if coord not in visited:
                    flag = True
                    visited.add(coord)
                    for sensorBeacon in sensorBeaconCombos:
                        sensor3 = sensorBeacon[0]
                        beacon3 = sensorBeacon[1]
                        if calculate_radius(sensor3, coord) <= calculate_radius(sensor3, beacon3): 
                            flag = False
                            break
                        
                    if flag == True and coord[0] >= 0 and coord[0] <= 4000000 and coord[1] >= 0 and coord[1] <= 4000000: return coord
                            
print(f'Part 1: {part1()}')
answPart2 = part2()
print(f'Part 2: {answPart2[0] * 4000000 + answPart2[1]}')