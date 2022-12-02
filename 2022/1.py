with open('input/1.txt', 'r') as file:
    data = file.read()
split = data.split('\n\n')

maxCaloriesCarried = 0
elfNum = -1

for index, s in enumerate(split, start=1):
    calories = s.split("\n")
    calories = [eval(i) for i in calories]
    totalCalories = sum(calories)
    if totalCalories > maxCaloriesCarried:
        maxCaloriesCarried = totalCalories
        elfNum = index
        
print(maxCaloriesCarried)
print(elfNum)