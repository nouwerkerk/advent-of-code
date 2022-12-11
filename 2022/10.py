def part1(data):
    cycle = 0
    register = 1
    signalStrength = 0
            
    for line in data:

        cycle += 1
        if (cycle - 20) % 40 == 0:
            signalStrength += (register * cycle)    
        
        if line == 'noop':
            continue
        else:
            splittedLine = line.split()
            num = int(splittedLine[1])
            
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signalStrength += (register * cycle)
            
            register += num

    return signalStrength

def part2(data):
    cycle = 0
    register = 1
    result = []
    row = []
    
    def addChar(CRTposition):
        if CRTposition in range(register - 1, register + 2):
            row.append('#')
        else:
            row.append('.')
    
    for line in data:
        
        CRTposition = cycle % 40
        
        if line == 'noop':
            addChar(CRTposition)
            cycle += 1
        
        else:
            splittedLine = line.split()
            num = int(splittedLine[1])
            
            addChar(CRTposition)
            cycle += 1
            
            if cycle != 0 and cycle % 40 == 0:
                result.append(row)
                row = []
    
            CRTposition = cycle % 40
            
            addChar(CRTposition)
            cycle += 1
            register += num
            
        if cycle != 0 and cycle % 40 == 0:
            result.append(row)
            row = []
    
    return result
    
with open('example-input/10.txt', 'r') as file:
   data = file.read().splitlines()
file.close()

print(f"Part 1: {part1(data)}")
print(f"Part 2:")

result = part2(data)
for row in result:
    string = ''
    for char in row:
        string += char
    print(string)