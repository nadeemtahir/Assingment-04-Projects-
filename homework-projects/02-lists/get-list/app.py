def get_list():
    items = []

    print("📋 List Builder")
    print("➤ Enter elements one by one.")
    print("➤ Type 'stop' anytime to finish.\n")

    while True:
        user_input = input("🔹 Enter item: ").strip()

        if user_input == "":
            print("⚠️  Empty input is not allowed. Try again.\n")
            continue

        if user_input.lower() == "stop":
            break

        items.append(user_input)
        print(f"✅ '{user_input}' added to the list.\n")

    if items:
        print("\n✅ Final List:", items)
        print(f"📦 Total items: {len(items)}")
    else:
        print("\n🚫 No items were added to the list.")

# Call the function
get_list()
