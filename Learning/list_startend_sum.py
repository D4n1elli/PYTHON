# Challenge: sum the first and last number of a list
#02/03/2026 :)

# Gets the input of the list numbers
def input_numbers():
    numbers = []

    i = 0
    while True:
        numinput = (int(input(f"N {i + 1}: ")))
        if (numinput == 0):
            break

        numbers.append(numinput)
        i += 1

    return numbers


def sum_start_end():

    numbers = input_numbers()
    if len(numbers) < 2:
        print("Type at least 2 numbers")
        numbers = input_numbers()


    nums_sum = numbers[0] + numbers[len(numbers) - 1] 

    print(f"The numbers you typed are: {numbers}")
    print(f"And the sum of the first and last element is: {nums_sum}")


print("Type how many numbers you like, type 0 to stop")
sum_start_end()