import string

#values of all letters
values = dict()
for index, letter in enumerate(string.ascii_letters, 1):
   values[letter] = index

def part1():
   with open('example-input/3.txt', 'r') as file:
      data = [(l[:len(l) // 2], l[len(l) // 2:]) for l in file.read().splitlines()]
   file.close()

   #flatten sets into single list
   similarElems = [x for (a, b) in data for x in set(a).intersection(set(b))]

   points = sum([values[letter] for letter in similarElems])
   return points

def part2():
   with open('example-input/3.txt', 'r') as file:
      data = [l for l in file.read().splitlines()]
   
   groups = []
   for i in range(0, len(data) - 1, 3):
      groups.append((data[i], data[i + 1], data[i + 2]))
   
   similarElems = [x for (a, b, c) in groups for x in set(c).intersection(set(a).intersection(set(b)))]
   
   points = sum([values[letter] for letter in similarElems])
   return points
   
print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")