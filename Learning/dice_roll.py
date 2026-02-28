import random

# 19/02/2026

# rolls the dice (1 to 6)
def roll_dice():
    dices_rolled = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    return dices_rolled

# Gets the user input of if they want to continue to roll the dice
def continue_roll_input():
    while True:
        roll = int(input())

        if roll < 0 or roll > 1:
            print("Please digit a valid number.")
            continue
        else: break
            
    return roll

#prints jackpot if all numbers are equal
def luck_printer():
    dices_rolled = roll_dice()
    print(dices_rolled)

    if dices_rolled[0] == dices_rolled[1] == dices_rolled[2]:
        print("Jackpot!")



def main():
    print("\nDigit 1 to roll the dice!")
    print("Digit 0 to quit.")
    while True:
        again = continue_roll_input()

        if again == 0:
            break
        
        luck_printer()

main()
print("Quitting...")