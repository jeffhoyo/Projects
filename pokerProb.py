import os
import math

# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# Sample Space
cards = 52

# Determine the probability of drawing a heart
hearts = 13
heart_probability = event_probability(hearts, cards)

# Determine the probability of drawing a face card
face_cards = 12
face_card_probability = event_probability(face_cards, cards)

# Determine the probability of drawing the queen of hearts
queen_of_hearts = 1
queen_of_hearts_probability = event_probability(queen_of_hearts, cards)

os.system("clear")

# Print each probability
print(str(heart_probability) + "%")
print(str(face_card_probability) + "%")
print(str(queen_of_hearts_probability) + "%")
print("")
# Permutations Code
n = 4
k = 2

# Determine permutations and print result
Permutations = math.factorial(n) / math.factorial(k)
print(Permutations)
