def solve(data):
    score = 0
    for (v1, v2) in data:
        score += v2
        score += (v2 - v1 + 1) * 3 if abs(v2 - v1) in range (0, 2) else ((v2 - v1) / 2 + 1) * 3
    return score

valuedict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

with open('input/2.txt', 'r') as file:
    data = [(valuedict[l[0]], valuedict[l[2]]) for l in file.readlines()]
    
print(solve(data))
    
