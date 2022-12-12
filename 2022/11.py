import math

class Monkey():
    def __init__(self, startItems, operation, test, throwTrue, throwFalse):
        
        self.items_ = startItems
        self.operation_ = operation #string, when old is defined and eval() is used gives new worry 
        self.test_ = test #number that it should be divisable by
        self.throwTrue_ = throwTrue
        self.throwFalse_ = throwFalse
        
    def addItem(self, item):
        self.items_.append(item)
    
    def grabItem(self):
        return self.items_.pop(0)
        
def parseMonkey(textMonkey):
    lines = textMonkey.split('\n')
    
    startItems = [int(x.replace(',', '')) for x in lines[1].split(' ') if x.replace(',', '').isdigit() == True]
    operation = lines[2].replace('  Operation: new = ', '')
    test = int(lines[3].replace('Test: divisible by ',''))
    throwT = int(lines[4].replace('If true: throw to monkey ',''))
    throwF = int(lines[5].replace('If false: throw to monkey ',''))
    
    return Monkey(startItems, operation, test, throwT, throwF)

def calculate(data, isPart1 = True):
    monkeys = []
    counts = []
    
    for monkeyText in data:
        monkeys.append(parseMonkey(monkeyText))
        counts.append(0)
        
    combinedModulos = 1
    for monkey in monkeys:
        combinedModulos = combinedModulos * monkey.test_ 

    numRounds = 20
    if isPart1 == False:
        numRounds = 10000

    for _ in range(0, numRounds):
        for idx, monkey in enumerate(monkeys):
            while monkey.items_:
                counts[idx] += 1
                
                old = monkey.grabItem()
                worry = eval(monkey.operation_)
                if isPart1 == True:
                    worry = math.floor(worry / 3)
                else:
                    worry = worry % combinedModulos
                
                if worry % monkey.test_ == 0:
                    monkeys[monkey.throwTrue_].addItem(worry)
                else:
                    monkeys[monkey.throwFalse_].addItem(worry)

    counts.sort(reverse=True)
    return counts[0] * counts[1]

with open('example-input/11.txt', 'r') as file:
   data = [l for l in file.read().split('\n\n')]
file.close()

print(f"Part 1: {calculate(data)}")
print(f"Part 2: {calculate(data, isPart1=False)}")