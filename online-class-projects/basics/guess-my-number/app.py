import random

def guess_my_number():
    print("🎲 Guess My Number")
    secret_number = random.randint(0, 99)
    print("\nI am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess < secret_number:
                print("Your guess is too low\n")
            elif guess > secret_number:
                print("Your guess is too high\n")
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break
        except ValueError:
            print("❌ Please enter a valid number!\n")

# Run the game
guess_my_number()
