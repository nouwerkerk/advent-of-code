with open('input/4.txt', 'r') as file:
   data = [l.split(',') for l in file.read().splitlines()]
file.close()

result = 0

for pairs in data:
    splitRange1 = pairs[0].split('-')
    rooms1 = {i for i in range(int(splitRange1[0]), int(splitRange1[1]) + 1)}
    
    splitRange2 = pairs[1].split('-')
    rooms2 = {i for i in range(int(splitRange2[0]), int(splitRange2[1]) + 1)}
    
    if rooms1.issubset(rooms2) or rooms2.issubset(rooms1):
        result += 1
        
print(result)