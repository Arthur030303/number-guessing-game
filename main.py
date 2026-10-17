#Number Guessing Game Project no.1
import random


print("Number Guessing Game (1 to 10)")
print("1. Play")
print("2. Exit")
count = 0
choice = int(input("Enter your choice: "))
if choice == 1:
    number = random.randint(1,10)
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
            playAgain = input("Play Again? (y/n): ").lower()
            if playAgain != "y":
                print("Thank you for playing.")
                break
            else:
                count = 0
                number = random.randint(1,10)
elif choice == 2:
    print("You have exited the game.")

    
