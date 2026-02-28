# Challenge: find the smallest number that is divisible by all numbers from 1 to 20


def smallest_multiple():
    x = 20
    divisor = 2 # every number is a multiple of 1, so it can be ignored

    while divisor <= 20:
        if x % divisor == 0:
            divisor += 1
        
        else:
            x += 1
            divisor = 2
            continue

    return x


answer = smallest_multiple()
print(answer)