import random

def print_random_numbers():
    print("🔢 10 Random Numbers:\n")

    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=" ")

    print()  # For a clean newline at the end

# Run the function
print_random_numbers()
