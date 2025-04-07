def leap_year():
    print("📅 Question No. 03 - Leap Year Checker")
    print("──────────────────────────────────────\n")

    # Get year from user with validation
    try:
        year = int(input("🔢 Please enter a year to check: "))
        if year <= 0:
            print("⚠️ Please enter a positive number for the year.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a valid year as a number.")
        return

    print(f"\n🔍 Checking if {year} is a leap year...")

    # Leap year logic
    if (year % 400 == 0):
        print("✅ Yes! It's a leap year because it's divisible by 400.")
    elif (year % 100 == 0):
        print("🚫 No, it's not a leap year because it's divisible by 100 but not by 400.")
    elif (year % 4 == 0):
        print("✅ Yes! It's a leap year because it's divisible by 4.")
    else:
        print("🚫 No, it's not a leap year because it's not divisible by 4.")

# Run the function
leap_year()
