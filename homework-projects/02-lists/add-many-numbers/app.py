def add_many_numbers(numbers: list[int]) -> int:
    sum_of_numbers: int = 0 
    for number in numbers:  
        sum_of_numbers += number  
    return sum_of_numbers  


def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  
    sum_of_numbers: int = add_many_numbers(numbers)  
    print(sum_of_numbers)
    

if __name__ == '__main__':
    main()
