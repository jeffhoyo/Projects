# Roll The Dice Game to digitize and support internal gambling habits.

import os
import random
import counter
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

def possibleNumbers():

    d4    = [1, 2, 3, 4]
    d6    = [1, 2, 3, 4, 5, 6]
    d8    = [1, 2, 3, 4, 5, 6, 7, 8]
    d10   = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    d12   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    d0090 = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]

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

counter = 0
roll = []
os.system("clear")
print("Rolling Dice 230,400 times...")
print("")

while (counter < 130):
    roll.append(diceRoll())
    counter += 1

roll.sort()
print("High Score is: ", roll[-1])
print("Low Score is: ", roll[0])
print("")
print("4 has been rolled:", roll.count(4), "times.")
print("129 has been rolled:", roll.count(129), "times.")
print("")

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

def createBar():
    plt.bar(xAxis, yAxis, width = .5)
    plt.xlabel('Roll Total')
    plt.ylabel('Count of Roll')
    plt.title('Count of Roll Total')
    plt.show()

def createScatter():
    plt.scatter(xAxis, yAxis)
    plt.xlabel('Roll Total')
    plt.ylabel('Count of Roll')
    plt.title('Count of Roll Total')
    plt.legend()
    plt.show()

createPlot()
