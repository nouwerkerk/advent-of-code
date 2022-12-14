rockLocations = set()
sandLocations = set()
part2Y = 0

def addRocks(rockList):
    for rockStructure in rockList:
        for i in range(0, len(rockStructure) - 1):
            rockFrom = rockStructure[i]
            rockTo = rockStructure[i + 1]
            
            minX = min(rockFrom[0], rockTo[0])
            maxX = max(rockFrom[0], rockTo[0])
            minY = min(rockFrom[1], rockTo[1])
            maxY = max(rockFrom[1], rockTo[1])
            global part2Y
            if (maxY > part2Y):
                part2Y = maxY
            
            for a in range(minX, maxX + 1):
                for b in range (minY, maxY + 1):
                    rockLocations.add((a, b))

def checkIfFloor(location):
    return location[1] == part2Y + 2

def checkIfAbyss(location):
    for rockLocation in rockLocations:
        if rockLocation[0] == location[0] and rockLocation[1] > location[1]:
            return False
    return True

def checkIfOccupied(location, isPart1=True):
    return location in rockLocations or location in sandLocations or (isPart1 == False and checkIfFloor(location))

def dropSand(isPart1=True):
    currentLocation = (500, 0)
    while True:
        if checkIfAbyss(currentLocation) and isPart1:
            return False
        if not checkIfOccupied((currentLocation[0], currentLocation[1] + 1), isPart1):
            currentLocation = ((currentLocation[0], currentLocation[1] + 1))
        elif not checkIfOccupied((currentLocation[0] - 1, currentLocation[1] + 1), isPart1):
            currentLocation = (currentLocation[0] - 1, currentLocation[1] + 1)
        elif not checkIfOccupied((currentLocation[0] + 1, currentLocation[1] + 1), isPart1):
            currentLocation = (currentLocation[0] + 1, currentLocation[1] + 1)
        else:
            if (isPart1 == False and currentLocation == (500, 0)):
                return False
            sandLocations.add(currentLocation)
            return True

def calculate(isPart1=True):
    result = 0
    while (dropSand(isPart1)):
        result += 1
    
    if not isPart1: result += 1 
    return result
    
with open('example-input/14.txt', 'r') as file:
    lines = [l for l in file.read().splitlines()]
file.close()

rockTemp = []

for line in lines:
    rockStructure = line.split(' -> ')
    for idx, loc in enumerate(rockStructure):
        tuple([eval(x) for x in loc.split(',')])
        rockStructure[idx] = tuple([eval(x) for x in loc.split(',')])

    rockTemp.append(rockStructure)
    
addRocks(rockTemp)

print(f"Part 1: {calculate()}")
sandLocations = set()
print(f"Part 2: {calculate(isPart1=False)}")