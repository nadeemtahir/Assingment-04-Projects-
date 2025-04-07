def add_three_copies(my_list, data):
    print("\n[Inside Function] Adding 3 copies of:", data)
    for i in range(3):  # Only add 3 copies
        print(f"  Copy {i+1}: Adding '{data}' to the list")
        my_list.append(data)
    print("[Inside Function] Current list inside function:", my_list)

def main():
    message = input("Enter a message to copy: ")
    my_list = []

    print("\n[Before Function] List Before:", my_list)

    # Call the function — list is passed by reference
    add_three_copies(my_list, message)

    print("\n[After Function] List After:", my_list)

if __name__ == '__main__':
    main()
