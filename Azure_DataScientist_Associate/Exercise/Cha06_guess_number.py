# implement a number guessing game
import random

count = 0
number = random.randint(1, 5)
is_continue = True

while is_continue:
    count += 1
    guess = input("Guess a number between 1 and 5: ")
    if guess != str(number):
        continue
    else:
        print("You guessed it in ", count, " tries!")
        is_continue = False
