def first_n_even_numbers():
    print("🔢 Question No 02 - First N Even Numbers\n")

    while True:
        try:
            user_input = input("How many even numbers do you want to print? (Press Enter to exit): ")
            if user_input == "":
                print("👋 Exiting. Have a great day!")
                break

            count = int(user_input)
            if count <= 0:
                print("⚠️ Please enter a number greater than 0.")
                continue

            print(f"\nHere are the first {count} even numbers:\n")
            for i in range(count):
                print(f"{i + 1}: {2 * i}")  # even numbers: 0, 2, 4, ...

        except ValueError:
            print("❌ Please enter a valid number.\n")

# Run the function
first_n_even_numbers()
