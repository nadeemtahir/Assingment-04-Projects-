def get_last_element():
    elements = []

    print("Enter elements one by one. Type 'stop' to finish.\n")

    while True:
        user_input = input("Enter an element (or type 'stop' to finish): ").strip()

        if user_input == "":
            print("⚠️  Empty input is not allowed. Please try again.\n")
            continue

        if user_input.lower() == "stop":
            break

        elements.append(user_input)
        print(f"✅ '{user_input}' added to the list.\n")

    if elements:
        print("\n📝 Final List:", elements)
        print(f"🔚 The last element of the list is: '{elements[-1]}'")
    else:
        print("\n🚫 No elements were added to the list.")

# Call the function
get_last_element()
