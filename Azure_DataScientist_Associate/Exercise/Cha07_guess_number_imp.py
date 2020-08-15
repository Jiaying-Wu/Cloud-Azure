# improve the number guessing game
import random

count = 0
guess = 0
actual = random.randint(1, 10)

print("Guess a number between 1 and 10")

while guess != actual:
    count += 1
    guess = input(f"Enter guess #{count}: ")
    if not guess.isnumeric():
        print("Numbers only, please!")
    elif int(guess) > actual:
        print("Your guess is too high, try again!")
    elif int(guess) < actual:
        print("Your guess is too low, try again!")
    else:
        break
print(f"You guessed it in {count} tries!")
