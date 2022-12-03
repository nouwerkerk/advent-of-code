import string

#values of all letters
values = dict()
for index, letter in enumerate(string.ascii_letters, 1):
   values[letter] = index

with open('input/3.txt', 'r') as file:
   data = [(l[:len(l) // 2], l[len(l) // 2:]) for l in file.read().splitlines()]

#flatten sets into single list
similarElems = [x for (a, b) in data for x in set(a).intersection(set(b))]

points = sum([values[letter] for letter in similarElems])
print(points)
