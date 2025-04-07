def shorten_list():
    items = []
    max_length = 3

    print("📝 Limited List Builder")
    print(f"➤ You can only keep the last {max_length} items.")
    print("➤ Type 'stop' to finish.\n")

    while True:
        user_input = input("🔹 Enter an item: ").strip()

        if user_input == "":
            print("⚠️  Empty input is not allowed. Please try again.\n")
            continue

        if user_input.lower() == "stop":
            break

        items.append(user_input)
        print(f"✅ '{user_input}' added to the list.")

        # Trim list if it exceeds max_length
        if len(items) > max_length:
            removed = items.pop(0)
            print(f"❌ List limit exceeded. Removed oldest item: '{removed}'")

        print(f"📌 Current list: {items}\n")

    print("\n✅ Final list (max length maintained):", items)

shorten_list()