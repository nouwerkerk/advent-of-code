def getResult(data):
    for i, _ in enumerate(data):
        if (i + 3 < len(data)):
            letters = {data[i], data[i+1], data[i+2], data[i+3]}
            if len(letters) == 4:
                return i + 4
            

with open('input/6.txt', 'r') as file:
   data = file.readline()
file.close()

print(getResult(data))