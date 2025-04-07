def fibonacci(n, memo={}):
    """
    Returns the nth Fibonacci number using memoization for better performance
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def fibonacci_range():
    """
    Asks the user for the length of the Fibonacci sequence to generate and displays the sequence.
    """
    print("🔢 Question No. 01 - Fibonacci Sequence\n")

    while True:
        try:
            user_input = int(input("How many Fibonacci numbers would you like to see? "))
            if user_input <= 0:
                print("⚠️ Please enter a positive number greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    print(f"\nHere are the first {user_input} Fibonacci numbers:\n")
    
    for i in range(user_input):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

# Run the function
fibonacci_range()
