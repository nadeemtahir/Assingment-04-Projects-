def international_voting_age():
    print("🗳️ Question No. 02 - International Voting Eligibility")
    print("────────────────────────────────────────────────────\n")

    # Voting age requirements by country
    VOTING_AGE_PETURKSBOUIPO = 16
    VOTING_AGE_STANLAU = 25
    VOTING_AGE_MAYENGUA = 48

    # Ask for user input
    try:
        age = int(input("🎂 How old are you? "))
        if age < 0:
            print("⚠️ Age cannot be negative.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        return

    print("\n📊 Based on your age:")

    # Check eligibility from highest to lowest threshold
    if age >= VOTING_AGE_MAYENGUA:
        print(f"✅ You can vote in 🇲🇾 MAYENGUA (Voting age: {VOTING_AGE_MAYENGUA})")
    elif age >= VOTING_AGE_STANLAU:
        print(f"✅ You can vote in 🇸🇹 STANLAU (Voting age: {VOTING_AGE_STANLAU})")
    elif age >= VOTING_AGE_PETURKSBOUIPO:
        print(f"✅ You can vote in 🇵🇹 PETURKSBOUIPO (Voting age: {VOTING_AGE_PETURKSBOUIPO})")
    else:
        print("🚫 You are not eligible to vote in any of these countries.")

# Run the function
international_voting_age()
