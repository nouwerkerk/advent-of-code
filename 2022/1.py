input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
split = input.split("\n\n")

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