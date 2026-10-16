#Number Guessing Game Project no.1
import random

number = random.randint(1,10)
count = 0
print("Number Guessing Game (1 to 10)")
while True:
    count += 1
    guess = int(input("Enter your guess number: "))
    if number > guess:
        print("Higher")
    elif number < guess:
        print("Lower")
    else:
        print("You have guessed the number! Congratulations!")
        print(f"The number of guesses you took is: {count}")
        break
