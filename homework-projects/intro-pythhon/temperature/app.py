def main():

    farhenheit = float(input("Enter temperature in farhenheit: "))
    celsius = (farhenheit - 32) * 5.0/9.0

    print(f"Temperature in celsius is: {celsius}")

if __name__ == "__main__":
    main()    