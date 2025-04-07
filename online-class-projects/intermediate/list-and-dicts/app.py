# ================== Problem No 01 =====================

def list_practice():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("List:", fruit_list)
    fruit_length = len(fruit_list)
    print(f"Length of the list: {fruit_length}")
    fruit_list.append("mango")
    print(f"Updated List: {fruit_list}")

# list_practice()


# ================= Problem No 02 =====================


# ============== Accessing Elements: ===================
def accessing_elements(elements_list):
    try:
        access_element = int(input("Which element would you like to access? Please enter the index number: "))
        print(f"Here is your element: {elements_list[access_element]}")
    except IndexError as e:
        print(f"Index Error: {e}. The index is out of range.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# ============ # Modifying Elements ===================
def modifying_elements(elements_list):
    try:
        access_element = int(input(f"Which element do you want to modify in the list? Please enter the index number: "))
        print(f"Here is your element: {elements_list[access_element]}")
        new_value = input("Enter the new value for this element: ")
        elements_list[access_element] = new_value
        print(f"Updated list: {elements_list}")
    except IndexError as e:
        print(f"Index Error: {e}. The index is out of range.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# ============ # Slicing Elements ===================
def slicing_elements(elements_list):
    try:
        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))
        sliced = elements_list[start_index:end_index]
        print(f"Here is the sliced list: {sliced}")
    except IndexError as e:
        print(f"Index Error: {e}. The indices are out of range.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")


# ==================== Index Game ========================
def index_game():
    elements_list = ["Zoha", 20, True, 20.5, 1j]
    print(f"Here is the list: {elements_list}")

    while True:
        print("\nChoose an operation: access, modify, slice, exit")
        operation = input("Enter operation: ").lower()

        if operation == "access":
            accessing_elements(elements_list)
        elif operation == "modify":
            modifying_elements(elements_list)
        elif operation == "slice":
            slicing_elements(elements_list)
        elif operation == "exit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid operation. Please enter a valid operation (access, modify, slice, or exit).")

# Uncomment to run the index game
index_game()
