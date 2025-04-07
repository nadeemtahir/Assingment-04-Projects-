from hashlib import sha256

def hash_password(password_to_check):
    """
    Hash the password using SHA-256 for secure storage
    """
    return sha256(password_to_check.encode()).hexdigest()


def login(email, stored_logins, password_to_check):
    """
    Check if the hashed password matches the stored login credentials
    """
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        print(f"✅ Login successful for {email}")
    else:
        print(f"❌ Login failed for {email}")


def user_data():
    """
    Main function to manage user logins, add new users, or reset passwords
    """
    print("🔐 Question No. 03 - Powerful Passwords")
    print("─────────────────────────────────────\n")

    stored_logins = {
        "alice@coffee.com": hash_password("password"),
        "bob@coffee.com": hash_password("espresso"),
    }

    # Functionality options
    while True:
        print("\nPlease choose an action:")
        print("1️⃣ Login")
        print("2️⃣ Add a New User")
        print("3️⃣ Reset Password")
        print("4️⃣ Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Login functionality
            email = input("📧 Enter your email: ").strip()
            password = input("🔑 Enter your password: ").strip()
            login(email, stored_logins, password)

        elif choice == "2":
            # Add a new user
            email = input("📧 Enter the email for the new user: ").strip()
            if email in stored_logins:
                print(f"⚠️ This email is already registered.")
                continue
            password = input("🔑 Enter the password for the new user: ").strip()
            stored_logins[email] = hash_password(password)
            print(f"✅ New user {email} added successfully!")

        elif choice == "3":
            # Reset password
            email = input("📧 Enter your email to reset password: ").strip()
            if email not in stored_logins:
                print(f"❌ No account found with {email}.")
                continue
            new_password = input("🔑 Enter your new password: ").strip()
            stored_logins[email] = hash_password(new_password)
            print(f"✅ Password for {email} has been successfully reset!")

        elif choice == "4":
            # Exit the program
            print("👋 Thank you for using the secure login system. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a valid option (1-4).")

# Run the user_data function
user_data()
