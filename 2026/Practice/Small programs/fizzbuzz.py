# 16/02/2026

#FizzBuzz

def fizzbuzz_calculating():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz", end=" ")
        elif i % 5 == 0:
            print("buzz", end=" ")
        elif i % 3 == 0:
            print("fizz", end=" ")
        else:
            print(i, end=" ")

        if i % 10 == 0:
            print("")

def main():
    print("FizzBuzz coding challenge:")
    print("Print every number from 1 to 100, replacing the multiples of 3 with 'fizz',")
    print("multiples of 5 with 'buzz' and multiples of both with 'fizzbuzz'")

    fizzbuzz_calculating()


main()