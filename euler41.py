import math

def prime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def pandigital(i):
    i = str(i)
    n = len(i)
    n = [str(j) for j in range(1, n+1)]

    if all([j in n for j in i]) and all([i.count(j) == 1 for j in n]):
        return True
    
    else:
        return False

m = 0

for i in range(123, 987654322):
    if pandigital(i):
        if prime(i):
            m = i
            print(i)

print(m)
