#Number Guessing Game Project no.1
import random

number = random.randint(1,10)

while True:
    guess = int(input("Enter your guess number: "))
    if number > guess:
        print("Higher")
    elif number < guess:
        print("Lower")
    else:
        print("You have guessed the number! Congratulations!")
        break