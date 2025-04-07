def phonebook():
    print("📖 Question No. 01 - Phonebook")
    print("──────────────────────────────\n")

    contact_list = {}

    # Take user name and phone number
    while True:
        user_name = input("👤 Enter your name (Press Enter to exit): ").strip()
        if user_name == "":
            print("👋 Goodbye! Exiting the phonebook...")
            break

        # Check if name already exists in the contact list
        if user_name in contact_list:
            print(f"⚠️ {user_name} is already in the phonebook.")
            continue

        while True:
            user_number = input("📞 Enter your mobile number (11 digits): ").strip()
            if len(user_number) == 11 and user_number.isdigit():
                contact_list[user_name] = user_number
                print(f"✅ Contact for {user_name} added successfully!")
                break
            else:
                print("❌ Invalid number! Please enter exactly 11 digits.")

    # Display all contacts
    if len(contact_list) > 0:
        print("\n📋 Contact List:")
        for idx, (name, number) in enumerate(contact_list.items(), 1):
            print(f"{idx}. {name} : {number}")
    else:
        print("⚠️ No contacts found in the phonebook!")

    # Search for a contact
    search_numbers(contact_list)

    return contact_list


def search_numbers(contact_list):
    print("\n🔍 Search Contact Numbers")
    search_name = input("🔎 Enter name to search: ").strip()

    if search_name.capitalize() in contact_list:
        print(f"\n✅ {search_name.capitalize()}'s Number: {contact_list[search_name.capitalize()]}")
    else:
        print(f"❌ No contact found for {search_name.capitalize()}.")

# Run the phonebook function
phonebook()
