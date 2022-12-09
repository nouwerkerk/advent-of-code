from textwrap import wrap
import math

def parseMoves(moves):
    parsedMoves = []
    for move in moves:
        split = move.split()
        parsedMoves.append( (int(split[1]), int(split[3]), int(split[5])) )
    return parsedMoves

def parseBlocks(blocks):
    stacks = []
    amountOfStacks = math.ceil(len(blocks[0]) / 4)
    for _ in range(amountOfStacks):
        stacks.append([])
    
    #highest block in stack is at index 0
    for line in blocks:
        for count, i in enumerate(range(0, len(line), 4)):
            lineSplit = line[i:i+4]

            if lineSplit.startswith('['):
                letter = lineSplit[1]
                stacks[count].append(letter)
    
    return stacks
        
with open('input/5.txt', 'r') as file:
   data = [l for l in file.read().splitlines()]
file.close()

moves = [x for x in data if x.startswith('move')]
blocks = [x for x in data if x.startswith('[') or x.startswith('  ')]

stacks = parseBlocks(blocks)
moves = parseMoves(moves)

for move in moves:
    amount = move[0]
    moveFrom = move[1]
    moveTo = move[2]
    for _ in range(amount):
        movedBlock = stacks[moveFrom - 1].pop(0)
        stacks[moveTo - 1].insert(0, movedBlock)

result = ''
for stack in stacks:
    result += stack[0]
    
print(result)
    
    