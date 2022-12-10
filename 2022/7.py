import sys

class Node:
    def __init__(self, name, parent, isDirectory):
        self.name_ = name
        self.children_ = []
        self.parent_ = parent
        self.size_ = 0
        self.isDirectory_ = isDirectory
        
    def append_child(self, node):
        self.children_.append(node)
        
    def get_parent(self):
        return self.parent_
    
    def get_child(self, name):
        for child in self.children_:
            if child.name_ == name:
                return child
            
    def add_size(self, amount):
        self.size_ += amount
        
    def __str__(self):
        l = "["
        for node in self.children_:
            l += str(node)
            l += ", "
        l += "]"
        return f"Node(\'{self.name_}\', {l}, {self.size_}, {self.isDirectory_})"
        
            
def calculate_size(node):
    if node.isDirectory_ == False:
        return node.size_
    
    if len(node.children_) == 0:
        return 0
    
    size = 0
    for child in node.children_:
        size += calculate_size(child)
        
    node.add_size(size)
    return size

def setup_tree(data):
    root = data.pop(0)
    currentNode = Node("/", None, True)

    for line in data:
        splitted = line.split(' ')

        if splitted[0] == '$':
            if splitted[1] == 'cd':
                if splitted[2] == '..':
                    currentNode = currentNode.get_parent()
                else:
                    currentNode = currentNode.get_child(splitted[2])
                
        else:
            if splitted[0] == 'dir':
                currentNode.append_child(Node(splitted[1], currentNode, True))
            else: 
                node = Node(splitted[1], currentNode, False)
                node.add_size(int(splitted[0]))
                currentNode.append_child(node)

    while currentNode.get_parent() is not None:
        currentNode = currentNode.get_parent()
    
    calculate_size(currentNode)
    return currentNode

def part1(node):
    if node.isDirectory_ == False:
        return 0
    
    totalSize = 0
    if node.size_ <= 100000:
        totalSize += node.size_
    
    for child in node.children_:
        totalSize += part1(child)
    
    return totalSize

def part2(node):
    if node.isDirectory_ == False:
        return sys.maxsize
    
    totalSize = tree.size_
    
    unusedSpace = 70000000 - (totalSize - node.size_)
    sizeChosenDir = sys.maxsize
    
    if unusedSpace >= 30000000:
        sizeChosenDir = min(sizeChosenDir, node.size_)

    for child in node.children_:
        sizeChosenDir = min(sizeChosenDir, part2(child))
        
    return sizeChosenDir
    

with open('example-input/7.txt', 'r') as file:
   data = file.read().splitlines()
file.close()

tree = setup_tree(data)
print(f"Part 1: {part1(tree)}")
print(f"Part 2: {part2(tree)}")