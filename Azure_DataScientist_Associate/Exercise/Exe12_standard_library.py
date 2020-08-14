import random
roll = random.randint(1, 10)
print(f'You rolled {roll}.')

# create an alias for the name of the module
import random as dice
roll = dice.randint(1, 10)
print(f'You rolled {roll}')