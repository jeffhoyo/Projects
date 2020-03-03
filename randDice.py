import random
import os
import matplotlib.pyplot as plt

def diceRoll():

    num_list = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    rand4    = random.randint(1, 4)
    rand6    = random.randint(1, 6)
    rand8    = random.randint(1, 8)
    rand10   = random.randint(0, 9)
    rand12   = random.randint(1, 12)
    rand0090 = random.choice(num_list)

    total = rand4 + rand6 + rand8 + rand10 + rand12 + rand0090
    return total

def randomDiceCount():

    randDice  = random.randint(1, 10)
    randSides = random.randint(1, 20)

    total = randDice * randSides
    return total

counter = 0
roll = []
os.system("clear")
rollCount = int(input("Number of rolls? "))
print("")
print("Rolling Dice", rollCount, "times...")
print("")
print(randomDiceCount())
print("")

while (counter < rollCount):
    roll.append((diceRoll() * randomDiceCount()))
    counter += 1

counter2 = 4
yAxis = []
while (counter2 < 130):
    yAxis.append(roll.count(counter2))
    counter2 += 1

counter3 = 4
xAxis = []
while (counter3 < 130):
    xAxis.append(counter3)
    counter3 += 1

def createPlot():
    plt.plot(xAxis, yAxis)
    plt.xlabel('Roll Total')
    plt.ylabel('Count of Roll')
    plt.title('Count of Roll Total')
    plt.show()

createPlot()
