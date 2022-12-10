def part1(data):
    score = 0
    for (v1, v2) in data:
        score += v2
        score += (v2 - v1 + 1) * 3 if abs(v2 - v1) in range (0, 2) else ((v1 - v2) // 2 + 1) * 3
    return score

def part2(data):
    score = 0
    for (v1, v2) in data:
        score += (v2 - 1) * 3
        score += ((v1 + v2 - 2) % 3) if ((v1 + v2 - 2) % 3) != 0 else 3
    return score

valuedict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

with open('real-input/2.txt', 'r') as file:
    data = [(valuedict[l[0]], valuedict[l[2]]) for l in file.readlines()]
file.close()

print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")