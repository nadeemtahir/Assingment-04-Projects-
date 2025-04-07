import random
import time

def computer_guess(x):
    print("🔮 Welcome to the Mind Reader Game!")
    print(f"Think of a number between 1 and {x}, and I’ll try to guess it...")
    print("Give me clues! Type:")
    print("  🔺 'H' if my guess is too High")
    print("  🔻 'L' if my guess is too Low")
    print("  ✅ 'C' if my guess is Correct")
    print("\nLet's begin!\n")
    
    low = 1
    high = x
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        attempts += 1
        time.sleep(0.7)  # just for a little suspense
        feedback = input(f"🤔 Is it {guess}? (H/L/C): ").lower()

        if feedback == 'h':
            high = guess - 1
            print("📉 Alright, I'll go lower.\n")
        elif feedback == 'l':
            low = guess + 1
            print("📈 Okay, I’ll go higher!\n")
        elif feedback == 'c':
            print("\n🎉 Woohoo! I guessed it right!")
            print(f"✅ Your number was {guess}.")
            print(f"🧠 It took me {attempts} tries to guess it!")
        else:
            print("❌ Invalid input. Please enter H, L, or C.")

# Run the game
computer_guess(100)
