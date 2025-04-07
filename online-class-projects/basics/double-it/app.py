def double_until_100():
    print("🔁 Double Until 100\n")

    try:
        user_input = int(input("Enter a number to begin doubling: "))
        curr_value = user_input

        if curr_value <= 0:
            print("❌ Please enter a number greater than 0.")
            return

        result_list = []

        while curr_value < 100:
            curr_value = curr_value * 2
            result_list.append(curr_value)

        # Display the results
        print("\nResult:")
        print(" ".join(str(num) for num in result_list))
        print(f"\n✅ We stop at {curr_value} because it is 100 or more.")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# Run the function
double_until_100()
