import random

# print enough dots to hide number from terminal
def dots_printing():
    for i in range(25):
        print(".")


def true_false_0_1(user_input):
    while True:
        if user_input == 0:
            return False
        elif user_input == 1:
            return True
        else:
            print("Type a valid number.")
            user_input = int(input("Back: "))
            continue


# main game
def main_game(start, end):
    correct_answer = random.randint(start, end)
    print(f"The number is: {correct_answer}")
    print("Type 1 when you are ready.\n")

    # input validation
    while True:
        ready = int(input("Ready: "))
        if ready == 1:
            break
        else:
            print("Digit a valid number.\n")
            continue

    # print dots for user to not see the number
    dots_printing()

    # asks for right number
    print("What was the number?")
    user_answer = int(input("Right number: "))

    # validation
    if user_answer == correct_answer:
        print("Correct! Back to menu? 1 for yes, 0 for no (quit).")
    else:
        print(f"Wrong! The answer was: {correct_answer}. Back to menu? 1 for yes, 0 for no (quit).")

    while True:
        x = int(input("Back: "))
        will_return = true_false_0_1(x)
        if will_return == True:
            main()
        else: return



# custom game input handling with validation and calls main game function
def custom_inputs():
    while True:
        start = int(input("Type the start number of your game: "))
        end = int(input("Type the end number of your game: "))
        print("\n")

        if start > end:
            print("Start must be smaller than end")
            continue
        elif start == end:
            print("Start and end cannot be equal.")
            continue
        else:
            break

    main_game(start, end)


# main
def main():
    # intro and rules print
    print("\n---Memory game---")
    print("Rules: a random number will appear, and you must type it correctly from memory")
    print("Do not scroll up back to check the number.\n")

    # menu printing and start, end and difficulty variables
    difs_number = 4 # change this if add more or remove difficulties.
    easy = [0, 1000]
    medium = [1000, 10000]
    hard = [10000, 100000]

    print("Difficulties:")
    print(f"1 - Easy: from {easy[0]} to {easy[1]}.\n2 - Medium: from {medium[0]} to {medium[1]}.")
    print(f"3 - Hard: from {hard[0]} to {hard[1]}.\n4 - Custom")

    # difficulty selection
    print("Please insert the number of the difficulty you want: ")

    while True:
        dif_selected = int(input())
        if dif_selected < 1 or dif_selected > difs_number:
            print("Please digit a valid difficulty\n")
            continue
        else: break

    # calling function with difficulty
    if dif_selected == 1:
        main_game(easy[0], easy[1])
    elif dif_selected == 2:
        main_game(medium[0], medium[1])
    elif dif_selected == 3:
        main_game(hard[0], hard[1])
    elif dif_selected == 4:
        # note: the main_game() function is called in custom_inputs() function
        print("Custom:")
        custom_inputs()


main()