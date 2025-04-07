import random

NUM_ROUNDS = 5  # You can change the number of rounds here

def get_valid_guess():
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if guess in ['higher', 'lower']:
            return guess
        print("Please enter either 'higher' or 'lower'.")

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------\n")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        user_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)

        print(f"Your number is {user_num}")
        guess = get_valid_guess()

        correct = (
            (guess == "higher" and user_num > comp_num) or
            (guess == "lower" and user_num < comp_num)
        )

        if correct:
            print(f"You were right! The computer's number was {comp_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        print(f"Your score is now {score}\n")

    print("Thanks for playing!\n")

    # Conditional end message
    if score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("👏 Good job, you played really well!")
    else:
        print("💡 Better luck next time!")

# Run the game
high_low_game()
