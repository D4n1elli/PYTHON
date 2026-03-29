# Challenge: create a program that takes integer numbers from the user and calculates the average
# The program is not allowed to accept negatives

def input_and_average():
    # numbers list
    numbers = []

    # loop to get inputs and sum
    total = 0
    while True:
        x = int(input(f"Number {len(numbers) + 1}: "))
        if x < 0:
            print("No negatives")
            continue
        if x == 0:
            if len(numbers) < 2:
                print("Please digit at least 2 numbers.")
                continue
            break

        numbers.append(x)
        total += x

    print(f"\nNumbers: {numbers}")
    return total / len(numbers)


def main():
    print("\n--Average Calculator--")
    print("Note: the program does not accept negatives. Digit 0 to stop.")

    average = input_and_average()
    print(f"Average: {average}")
main()



