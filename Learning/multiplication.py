# Exercise: make the program print the result of a multiplication without using the * operator


# Returns the result of the multiplication
def multiply(num1, num2):
    result = 0
    # loop to add num2 num1 times in result
    for i in range(num1):
        result += num2

    return result



# Main
def main():
    print("\n-Digit two numbers to multiplicate them!-")
    print("Digit 0 on both to finish the program")

    while True:
        number1 = int(input("First: "))
        number2 = int(input("Second: "))
        if number1 == 0 and number2 == 0:
            break

        result = multiply(number1, number2)

        print(f"{number1} x {number2} is equal to:")
        print(result)

    print("Finishing...")


main()
