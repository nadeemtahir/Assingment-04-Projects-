def double_it():
    print("🔁 Question No 05 - Double It\n")
    print("👉 Enter numbers to double them. When the total of all doubles exceeds 100, the loop will stop.\n")

    total = 0
    count = 1

    while True:
        try:
            user_input = input(f"[{count}] Enter a number (or press Enter to quit): ")
            if user_input.strip() == "":
                print("👋 You exited early. Final total was:", total)
                break

            user_number = int(user_input)
            double = user_number * 2
            total += double

            print(f"✅ {user_number} doubled is {double}. Running total: {total}\n")
            count += 1

            if total > 100:
                print(f"🎉 We stop at {total} because the total value exceeded 100. Great job!")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")

# Run the function
double_it()
