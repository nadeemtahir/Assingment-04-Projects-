import random

def guess_number():
    print("🎮 Question No. 00 - Guess My Number\n")
    
    # Difficulty levels
    print("Choose your difficulty level:")
    print("1️⃣ Easy (1 - 10)")
    print("2️⃣ Medium (1 - 50)")
    print("3️⃣ Hard (1 - 100)")

    while True:
        difficulty = input("Enter your choice (1, 2, 3): ").strip()

        if difficulty == "1":
            max_range = 10
            break
        elif difficulty == "2":
            max_range = 50
            break
        elif difficulty == "3":
            max_range = 100
            break
        else:
            print("⚠️ Invalid choice. Please choose a valid difficulty level.")

    # Secret number based on difficulty
    secret_number = random.randint(1, max_range)
    print(f"I am thinking of a number between 1 and {max_range}...")

    attempts = 0  # Count the number of attempts

    while True:
        try:
            user_guess = int(input("What is your guess? "))
            attempts += 1  # Increase attempts

            if user_guess < secret_number:
                print("⬇️ Your guess is too low.")
            elif user_guess > secret_number:
                print("⬆️ Your guess is too high.")
            else:
                print(f"🎉 Congrats! You found the number: {secret_number}")
                print(f"You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    # Option to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_number()
    else:
        print("👋 Thank you for playing! Goodbye.")

# Run the game
guess_number()
