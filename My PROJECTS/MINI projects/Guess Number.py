# lesson 1
# Simple guess the number game
import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the number.")
else:
    print(f"Sorry, the number was {number}. Better luck next time!")

            