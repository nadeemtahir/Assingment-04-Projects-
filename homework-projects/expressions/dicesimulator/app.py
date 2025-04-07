import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES) 
    die2 = random.randint(1, NUM_SIDES)  
    total = die1 + die2  
    print(f"You rolled {die1} and {die2} for a total of {total}")  

def main():
    
    die1 = 10
    print("The dice numb is " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()

    print("The thrice dice is " + str(die1))  

if __name__ == "__main__":
    main()
