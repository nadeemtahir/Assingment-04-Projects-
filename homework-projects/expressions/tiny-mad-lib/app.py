def main():
    SENTNECE_START = "Code in Place is fun. I learned to program and used Python to make my"

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    sentence = f"{SENTNECE_START} {adjective} {noun} and {verb}."

    print(sentence)


if __name__ == "__main__":
    main()