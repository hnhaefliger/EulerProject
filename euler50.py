import math

def prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

primes = [i for i in range(1000000) if prime(i)]
m = [0, 0]

for i in range(len(primes)):
    for j in range(len(primes)-i):
        s = sum(primes[i:j])

        if s in primes:
            if j > m[0]:
                m = [j, s, i, j]
                print(m)

        if s > 1000000:
            break
