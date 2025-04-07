import random
import string
from words import words
from hangman_visual import lives_visual_dict

# Colored output function
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    print(color("👻 Welcome to Hangman! Let's save your life by guessing the word... 🧠", "95"))
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(color("\n────────────────────────────", "90"))
        print(f"You have {color(str(lives), '92')} lives left. Used letters: {color(' '.join(sorted(used_letters)), '94')}")
        print(lives_visual_dict[lives])

        # Show current guessed word
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", color(' '.join(word_display), "96"))

        user_input = input(color("Guess a letter: ", "93")).upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                print(color("✔️ Good guess!", "92"))
            else:
                lives -= 1
                print(color(f"✖️ Nope! The letter {user_input} is not in the word.", "91"))
        elif user_input in used_letters:
            print(color("⚠️ You already used that letter. Try another one.", "93"))
        else:
            print(color("❌ Invalid input. Please enter a valid letter (A-Z).", "91"))

    print(color("\n════════════════════════════", "90"))
    if lives == 0:
        print(lives_visual_dict[lives])
        print(color(f"💀 Game over! You died. The word was: {word}", "91"))
    else:
        print(color(f"🎉 Congratulations! You guessed the word: {word}", "92"))

def play_game():
    while True:
        hangman()
        again = input(color("\n🔁 Do you want to play again? (y/n): ", "95")).lower()
        if again != 'y':
            print(color("👋 Thanks for playing Hangman. Stay alive! 💀", "95"))
            break

if __name__ == '__main__':
    play_game()
