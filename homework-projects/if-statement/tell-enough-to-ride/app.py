def tall_enough_to_ride():
    print("🎢 Question No. 04 - Ride Height Checker")
    print("────────────────────────────────────────\n")

    minimum_height = 50  # in inches

    while True:
        user_input = input("📏 How tall are you (in inches)? (Press Enter to exit): ").strip()

        if user_input == "":
            print("\n👋 Thanks for visiting the ride checker. Goodbye!")
            break

        try:
            user_height = int(user_input)

            if user_height <= 0:
                print("⚠️ Please enter a height greater than 0.\n")
                continue

            if user_height >= minimum_height:
                print("✅ You're tall enough to ride! Enjoy the thrill! 🎉\n")
            else:
                print("🚫 Sorry, you're not tall enough yet — maybe next year! 🐣\n")

        except ValueError:
            print("❌ Invalid input! Please enter your height as a number.\n")

# Run the function
tall_enough_to_ride()
