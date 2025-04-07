def main():
    num1 = int(input("Please enter an integer to be divided: "))  # Convert input to int
    num2 = int(input("Please enter an integer to divide by: "))  # Convert input to int

    quotient = num1 // num2  # Integer division
    remainder = num1 % num2  # Modulus operator gives remainder

    print(f"The quotient of {num1} divided by {num2} is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
