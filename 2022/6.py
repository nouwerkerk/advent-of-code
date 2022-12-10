def getResult(data, amountOfDistinct):
    for i, _ in enumerate(data):
        if (i + amountOfDistinct < len(data)):
            letters = set()
            for j in range(i, i + amountOfDistinct):
                letters.add(data[j])
                
            if len(letters) == amountOfDistinct:
                return i + amountOfDistinct
            

with open('example-input/6.txt', 'r') as file:
   data = file.readline()
file.close()

print(f"Part 1: {getResult(data, 4)}")
print(f"Part 2: {getResult(data, 14)}")     