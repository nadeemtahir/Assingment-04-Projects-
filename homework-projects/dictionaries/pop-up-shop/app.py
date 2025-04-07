def pop_up_shop():
    print("🛍️ Question No. 02 - Pop Up Shop")
    print("──────────────────────────────────\n")

    # Fruit prices dictionary
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }

    total = 0

    while True:
        print("\n🍊 Available Fruits:")
        for fruit, price in fruits.items():
            print(f"🍏 {fruit.capitalize()}: ${price} per unit")

        # Ask the user for quantity
        fruit_choice = input("\nWhich fruit would you like to buy? (Enter 'stop' to finish shopping) ").lower()

        if fruit_choice == "stop":
            print(f"\n💰 Your total amount so far is ${total:.2f}")
            print("👋 Thank you for visiting! Goodbye!")
            break

        if fruit_choice not in fruits:
            print("❌ Sorry, we don't have that fruit. Please choose from the available options.")
            continue

        while True:
            try:
                quantity = input(f"How many {fruit_choice}s would you like to buy? ").strip()
                if quantity == "":
                    print("⚠️ Please enter a valid quantity.")
                    continue
                if quantity.isdigit():
                    quantity = int(quantity)
                    if quantity <= 0:
                        print("⚠️ Quantity must be greater than 0.")
                        continue
                    total += fruits[fruit_choice] * quantity
                    print(f"✅ {quantity} {fruit_choice.capitalize()}(s) added to your cart.")
                    break
                else:
                    print("❌ Please enter a valid number.")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        view_or_checkout = input("\nDo you want to continue shopping (yes/no)? ").lower()
        if view_or_checkout == "no":
            print(f"\n💰 Your final total amount is ${total:.2f}")
            print("👋 Thank you for shopping with us!")
            break

# Run the pop-up shop function
pop_up_shop()
