# A = X = Rock (1)
# B = Y = Paper (2)
# C = Z = Scissor (3)

with open('input/2.txt', 'r') as file:
    data = file.read()

data = data.split('\n')

#win = 6
#tie = 3
#lose = 0

points = 0
for d in data:
    d = d.split(' ')
    
    if d[1] == 'X':
        points += 1
        if d[0] == 'A':
            points += 3
        if d[0] == 'B':
            points += 0
        if d[0] == 'C':
            points += 6
            
    if d[1] == 'Y':
        points += 2
        if d[0] == 'A':
            points += 6
        if d[0] == 'B':
            points += 3
        if d[0] == 'C':
            points += 0
            
    if d[1] == 'Z':
        points += 3
        if d[0] == 'A':
            points += 0
        if d[0] == 'B':
            points += 6
        if d[0] == 'C':
            points += 3

print(points)
