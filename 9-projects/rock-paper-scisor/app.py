import random

# For colored text
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def get_user_choice():
    while True:
        choice = input("Choose [r]ock, [p]aper, or [s]cissors: ").lower()
        if choice in ['r', 'p', 's']:
            return choice
        else:
            print(color_text("Invalid choice! Please choose 'r', 'p', or 's'.", "91"))

def convert_choice(choice):
    return {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}[choice]

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play_round():
    user = get_user_choice()
    computer = random.choice(['r', 'p', 's'])

    user_full = convert_choice(user)
    computer_full = convert_choice(computer)

    print(f"\nYou chose: {color_text(user_full, '94')}")
    print(f"Computer chose: {color_text(computer_full, '93')}")

    if user == computer:
        print(color_text("It's a tie!", "96"))
    elif is_win(user, computer):
        print(color_text("You won! 🎉", "92"))
    else:
        print(color_text("You lost! 😢", "91"))

def play():
    print(color_text("🎮 Welcome to Rock, Paper, Scissors Game! 🎮", "95"))
    while True:
        play_round()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print(color_text("Thanks for playing! 👋", "95"))
            break

play()
