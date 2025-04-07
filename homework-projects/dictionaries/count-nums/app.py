def count_nums():
    print("🔢 Question No. 00 - Count Numbers")
    print("────────────────────────────────────\n")

    store_numbers = []

    while True:
        user_input = input("📥 Enter a number (Press Enter to stop): ").strip()

        if user_input == "":
            print("👋 Goodbye! Thank you for using the counter!")
            break

        try:
            user_number = int(user_input)
            store_numbers.append(user_number)
            print(f"✅ Added {user_number} to the list.\n")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

    if store_numbers:
        print("\n📊 Number Frequencies (sorted):")
        for num in sorted(set(store_numbers)):
            print(f"🔢 {num} appears {store_numbers.count(num)} time(s)")

        return store_numbers
    else:
        print("⚠️ No numbers were entered.")
        return []

count_nums()
