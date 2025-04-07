def print_events():
    print("✨ Question 01 - Even Number Finder")
    print("────────────────────────────────────\n")

    # Ask the user how many numbers they want to check
    try:
        limit = int(input("🔢 Enter the upper limit (e.g., 20): "))
        if limit <= 0:
            print("⚠️ Please enter a number greater than zero.")
            return
    except ValueError:
        print("❌ Invalid input! Only enter whole numbers.")
        return

    even_numbers = []

    # Loop from 1 to the given limit and collect even numbers
    for number in range(1, limit + 1):
        if number % 2 == 0:
            even_numbers.append(number)

    # Show results
    print("\n🎯 Even numbers from 1 to", limit, "are:")
    print("👉", even_numbers)
    print(f"✅ Total even numbers found: {len(even_numbers)}")

# Run the function
print_events()
