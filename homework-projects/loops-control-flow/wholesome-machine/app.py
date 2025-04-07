import random

def wholesome_machine():
    print("💖 Question No 03 - Wholesome Machine\n")
    
    affirmations = [
        "I am capable of doing anything I put my mind to.",
        "I believe in myself and my abilities.",
        "I am strong, smart, and resilient.",
        "Every day is a fresh start.",
        "I radiate confidence and positivity."
    ]

    chosen_affirmation = random.choice(affirmations)
    print("✨ Today's affirmation challenge:")
    print(f"\n🔁 Please type the following affirmation exactly as shown:\n\n\"{chosen_affirmation}\"\n")

    while True:
        user_input = input("Your turn: ")
        if user_input.strip() == chosen_affirmation:
            print("\n✅ That's right! You're amazing! 🌟")
            break
        else:
            print("❌ Almost there! Try again — you got this 💪")

# Run it
wholesome_machine()
