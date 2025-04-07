import random
import time

def guess_number(x):
    print(f"\n🎯 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {x}. Can you guess it?\n")

    random_number = random.randint(1, x)
    attempts = 0

    while True:
        try:
            user_guess = int(input(f"🔢 Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > x:
                print(f"⚠️ Please guess a number between 1 and {x}.\n")
                continue

            if user_guess < random_number:
                print("📉 Too low! Try again.\n")
            elif user_guess > random_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"\n🎉 Congrats! You guessed the number {random_number} correctly in {attempts} attempts! 🥳")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

# Run the game
guess_number(10)
