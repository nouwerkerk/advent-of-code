import math

directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def updateTail(posList, idxHead, idxTail):
    dX = posList[idxHead][0] - posList[idxTail][0]
    dY = posList[idxHead][1] - posList[idxTail][1]
    if abs(dX) > 1 or abs(dY) > 1:
        moveBy = [0, 0]
        for idx, delta in enumerate([dX, dY]):
            if delta < 0:
                moveBy[idx] = math.floor(delta / 2)
            else:
                moveBy[idx] = math.ceil(delta / 2)
        
        posList[idxTail] = (posList[idxTail][0] + moveBy[0], posList[idxTail][1] + moveBy[1])

def part1(data):
    visitedPositions = set()
    positions = [(0, 0), (0, 0)]
    
    for line in data:
        splitLine = line.split(' ')
        
        for _ in range(0, int(splitLine[1])):
            direction = directions[splitLine[0]]

            positions[0] = (positions[0][0] + direction[0], positions[0][1] + direction[1])
            updateTail(positions, 0, 1)
            visitedPositions.add(positions[1])
    return len(visitedPositions)

def part2(data):
    visitedPositions = set()
    positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    
    for line in data:
        splitLine = line.split(' ')
        
        for _ in range(0, int(splitLine[1])):
            direction = directions[splitLine[0]]

            positions[0] = (positions[0][0] + direction[0], positions[0][1] + direction[1])
            
            for i in range(1, len(positions)):
                updateTail(positions, i - 1, i)
                
            visitedPositions.add(positions[9])
    return len(visitedPositions)


    
with open('example-input/9.txt', 'r') as file:
   data = file.read().splitlines()
file.close()

print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
