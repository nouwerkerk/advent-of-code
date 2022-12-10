def get_rooms(pairs):
    splitRange1 = pairs[0].split('-')
    rooms1 = {i for i in range(int(splitRange1[0]), int(splitRange1[1]) + 1)}
        
    splitRange2 = pairs[1].split('-')
    rooms2 = {i for i in range(int(splitRange2[0]), int(splitRange2[1]) + 1)}
    
    return rooms1, rooms2
    
def part1(data):
    result = 0
    for pairs in data:
        rooms1, rooms2 = get_rooms(pairs)
        if rooms1.issubset(rooms2) or rooms2.issubset(rooms1):
            result += 1
            
    return result

def part2(data):
    result = 0
    for pairs in data:
        rooms1, rooms2 = get_rooms(pairs)
        if len(rooms1.union(rooms2)) < len(rooms1) + len(rooms2):
            result += 1
            
    return result

with open('real-input/4.txt', 'r') as file:
   data = [l.split(',') for l in file.read().splitlines()]
file.close()

print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")