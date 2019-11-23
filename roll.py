import random

def roll(num_rolls, size):
    total = 0
    for i in range(num_rolls):
        total += random.randint(1, size)
    return total
