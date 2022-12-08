import numpy as np

def get_grid(path):
    with open(path, 'r') as file:
        data = [list(l) for l in file.read().splitlines()]
    file.close()
    
    grid = []
    for row in data:
        grid.append([int(num) for num in row])

    return np.array(grid)

def check_visible(row):
    for i in range(1, len(row)):
        if row[i] >= row[0]:
            return False
    return True
    
grid = get_grid('input/8.txt')
height, length = grid.shape

visibleTrees = 0

for idxHeight in range(1, height - 1):
    for idxLength in range(1, length - 1):
        currentNumber = grid[idxHeight][idxLength]
        isVisible = False
        
        #create slices for each direction i.r.t. the current tree, where the current tree is at position 0
        for directionSlice in [grid[idxHeight, 0:idxLength + 1][::-1], grid[idxHeight, idxLength:length], grid[0:idxHeight + 1, idxLength][::-1], grid[idxHeight:height, idxLength]]:
            isVisible = isVisible or check_visible(directionSlice) 
            
        if isVisible == True:
            visibleTrees += 1

edgeTrees = 2 * length + (2 * (height - 2))
visibleTrees += edgeTrees

print(visibleTrees)