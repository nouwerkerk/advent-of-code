import string
import sys

class Node():
    def __init__(self, level):
        self.level_ = level
        self.neighbours_ = []
        self.visitedVia_ = None
        
    def add_neighbour(self, node):
        self.neighbours_.append(node)
        
    def set_via(self, node):
        self.visitedVia_ = node
    
    def get_level(self):
        return self.level_

values = dict()
for index, letter in enumerate(string.ascii_lowercase, 1):
   values[letter] = index
values['S'] = 1
values['E'] = 27

def get_graph(data, isPart1 = True):
    height = len(data)
    width = len(data[0])
    graph = []
    startLocation = []
    
    for i in range(0, height):
        row = []
        for j in range(0, width):
            letter = data[i][j]
            node = Node(values[letter])
            row.append(node)
            if letter == 'S' or (letter == 'a' and isPart1 == False):
                startLocation.append(node)

        graph.append(row)
            
    return graph, startLocation

def setup_neighbours(graph):
    height = len(graph)
    width = len(graph[0])
    for i in range(0, height):
        for j in range(0, width):
            node = graph[i][j] #i = y-axis, j = x-axis
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newLoc = (i + direction[1], j + direction[0])
                if not (newLoc[0] < 0 or newLoc[1] < 0 or newLoc[0] > height - 1 or newLoc[1] > width - 1):
                    node.add_neighbour(graph[newLoc[0]][newLoc[1]])

def reset_graph(graph):
    for row in graph:
        for node in row:
            node.visitedVia_ = None

def BFS(data, isPart1 = True):
    graph, startNodes = get_graph(data, isPart1)
    setup_neighbours(graph)
    finalPathLength = sys.maxsize

    for n in startNodes:
        visited = []
        queue = []
        queue.append(n)
        visited.append(n)
        currentNode = None

        while queue:
            currentNode = queue.pop(0)
            if currentNode.get_level() == 27:
                break
            
            for neighbour in currentNode.neighbours_:
                if neighbour not in visited and neighbour.get_level() - currentNode.get_level() <= 1:
                    visited.append(neighbour)
                    neighbour.set_via(currentNode)
                    queue.append(neighbour)
        
        if currentNode.get_level() != 27:
            continue
        else:
            pathLength = 0
            while currentNode.visitedVia_ is not None:
                pathLength += 1
                currentNode = currentNode.visitedVia_
            if pathLength < finalPathLength:
                finalPathLength = pathLength
        
        reset_graph(graph)
        
    return finalPathLength
        
with open('example-input/12.txt', 'r') as file:
   data = [l for l in file.read().splitlines()]
file.close()

print(f"Part 1: {BFS(data)}")
print(f"Part 2: {BFS(data, isPart1=False)}")