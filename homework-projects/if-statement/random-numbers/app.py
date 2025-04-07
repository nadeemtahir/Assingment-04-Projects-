import random

def random_number():
    print("🎯 Question No. 05 - Random Number Generator")
    print("────────────────────────────────────────────\n")

    try:
        count = int(input("🔢 How many random numbers would you like to generate? "))
        if count <= 0:
            print("⚠️ Please enter a number greater than 0.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")
        return

    # Customize range here (1 to 100)
    min_val = 1
    max_val = 100

    numbers = []

    for _ in range(count):
        number = random.randint(min_val, max_val)
        numbers.append(number)

    print(f"\n🎰 Generated {count} random number(s) between {min_val} and {max_val}:")
    print("👉", numbers)

# Run the function
random_number()
