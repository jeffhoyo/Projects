# Roll The Dice Game to digitize and support internal gambling habits.

import os
import random

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
i       = 0
os.system("clear")
while (counter < 10):
    roll = []
    roll.append(diceRoll())
    print(roll)
    counter = counter + 1
    i = i + 1
