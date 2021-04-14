import math

def count_factors(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return [i] + count_factors(int(n/i))

    else:
        return [n]

numbers = [1, 2, 3, 4]
factors = [count_factors(number) for number in numbers]
i = 4

while any([a != 4 for a in factors]):
    i += 1
    numbers = numbers[1:] + [i]
    factors = factors[1:] + [len(set(count_factors(i)))]

print(numbers, factors)
