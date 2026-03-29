# Exercise: find all Fibonacci numbers from 1 to 1000
# 02/02/2026

# Function to calculate the numbers
def fibonacci_calculating():
    fibonacci_numbers = [1, 2]
    first = 1
    second = 2

    next_value = 0
    while(True):
        next_value = first+second
        if next_value > 1000:
            break
        fibonacci_numbers.append(next_value)
        first = second
        second = next_value

    print(fibonacci_numbers)
        

# Main
def main():
    print("\nAll Fibonacci numbers from 1 to 1000!")
    fibonacci_calculating()

main()