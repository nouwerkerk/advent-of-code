import ast
import itertools

def add_indent(str, indent):
    newStr = ''
    for _ in range(0, indent):
        newStr += ' '
    return newStr + str

def compareList(left, right, indent):
    #zip lists with, pad with None if unequal length
    zipLists = itertools.zip_longest(left, right)
    
    for (zipLeft, zipRight) in zipLists:
        if zipLeft == [] and zipRight == []: continue
        
        #if original lists are unequal length
        elif zipLeft == None: return True
        elif zipRight == None: return False
        
        #if both are integers 
        elif type(zipLeft) == int and type(zipRight) == int:
            if zipLeft < zipRight: return True
            elif zipLeft > zipRight: return False
            else: continue
        
        #if one is integer and other is list 
        elif type(zipLeft) == list and type(zipRight) == int:
            x = compareList(zipLeft, [zipRight], indent=indent+4)
            if x != None: return x

        elif type(zipLeft) == int and type(zipRight) == list:
            x = compareList([zipLeft], zipRight, indent=indent+2)
            if x != None: return x
        
        #if both are lists
        else:
            x = compareList(zipLeft, zipRight, indent=indent+2)
            if x != None: return x
    
    return None

def part1():
    with open('example-input/13.txt', 'r') as file:
        pairs = [l for l in file.read().split("\n\n")]
    file.close()
    
    result = 0

    for idx, pair in enumerate(pairs, 1):
        splitted = pair.split('\n')
        pair1 = ast.literal_eval(splitted[0])
        pair2 = ast.literal_eval(splitted[1])
        
        if compareList(pair1, pair2, indent=2):
            result += idx
    
    return result

def part2():
    with open('example-input/13.txt', 'r') as file:
        items = [ast.literal_eval(l) for x in file.read().split("\n\n") for l in x.split('\n')]
    file.close()

    items.append([[6]])
    items.append([[2]])
    
    packets = []
    
    for item in items:
        if len(packets) == 0: packets.append(item)
        else:
            flag = False
            idx = 0
            while idx < len(packets):

                if compareList(item, packets[idx], 2) == True:
                    flag = True
                    packets.insert(idx, item)
                    break
                idx += 1
            if flag == False:
                packets.append(item)

    return (packets.index([[6]]) + 1) * (packets.index([[2]]) + 1)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")