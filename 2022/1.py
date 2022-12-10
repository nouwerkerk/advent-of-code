def sort_calories(data):
    split = data.split('\n\n')

    sortedCalories = []

    for index, s in enumerate(split, start=1):
        calories = s.split("\n")
        calories = [eval(i) for i in calories]
        totalCalories = sum(calories)
        
        if len(sortedCalories) == 0:
            sortedCalories.append(totalCalories)
        else:
            for i in range(len(sortedCalories)):
                if totalCalories > sortedCalories[i]:
                    sortedCalories.insert(i, totalCalories)
                    break
                
    return sortedCalories

with open('example-input/1.txt', 'r') as file:
    data = file.read()
file.close()

print(f"Part 1: {sort_calories(data)[0]}")
print(f"Part 2: {sort_calories(data)[0] + sort_calories(data)[1] + sort_calories(data)[2]}")