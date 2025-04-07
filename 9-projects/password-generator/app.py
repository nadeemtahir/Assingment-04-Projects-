import random

# Colored output
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

# Character sets
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!@#$%&*().,?'

# Greet user
print(color("🔐 Welcome to Your Custom Password Generator! 🔐", "95"))

# Ask what to include
def yes_or_no(prompt):
    while True:
        choice = input(color(prompt + " (y/n): ", "93")).lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print(color("⚠️ Please type 'y' or 'n'.", "91"))

use_lower = yes_or_no("Include lowercase letters?")
use_upper = yes_or_no("Include uppercase letters?")
use_numbers = yes_or_no("Include numbers?")
use_symbols = yes_or_no("Include special characters?")

# Build the character set
chars = ''
if use_lower: chars += lowercase
if use_upper: chars += uppercase
if use_numbers: chars += numbers
if use_symbols: chars += symbols

if not chars:
    print(color("❌ You must choose at least one character type!", "91"))
    exit()

# Get user input safely
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(color(prompt, "94")))
            if value > 0:
                return value
            else:
                print(color("⚠️ Please enter a number greater than 0.", "91"))
        except ValueError:
            print(color("❌ Invalid input. Enter a whole number.", "91"))

count = get_positive_int("How many passwords would you like to generate? ")
length = get_positive_int("What should be the length of each password? ")

# Generate passwords
print(color("\n🧪 Generating your secure passwords...\n", "96"))
for i in range(count):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(color(f"[{i + 1}] ➤ {password}", "92"))

print(color("\n✅ All passwords generated successfully!", "92"))
print(color("💡 Tip: Use a password manager to safely store them.", "90"))
