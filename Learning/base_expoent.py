# Challenge: print the result of the base by the expoent

# Gets the input of the base and expoent and calculates the result
def power_calculator():

# -- input --
    base = int(input("Base: "))
    expoent = int(input("Expoent: \n"))

    # quit if one of them is 0
    if base == 0 or expoent == 0:
        return 0

# -- calculator --

    result = 1
    for i in range (expoent):
        result *= base


    return result



print("\nPlease insert the base and the expoent of the power")
print("Digit 0 in any of them to quit\n")
# loop until user wants to quit
power_result = 0
while True:
    power_result = power_calculator()

    # finish program if result is 0
    if power_result == 0:
        print("Finishing...\n")
        break

    # display result
    print(power_result)


