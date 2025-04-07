def get_first_element():
    store_list = []
    i = ""

    while True:
        i = input("Please enter an element of the list or type 'stop' to exit: ")

        if i == "":
            print("You cannot enter an empty input. ")
            continue

        if i.lower() == "stop":
            break

        store_list.append(i)


        if store_list:
            first_index = store_list[0]

    print(f"List is here: {store_list}")
    first_index = store_list[0]
    print(f"The first element of list is {first_index}")