import math

def permutations(x, y, z):
    x, y, z = str(x), str(y), str(z)

    for char in x:
        if char not in y or char not in z:
            return False

    return True

def prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

m = 3330

for c in range(1000, 3340):
    x, y, z = c, c+m, c+2*m

    if prime(x) and prime(y) and prime(z) and permutations(x, y, z):
        print(x, y, z, m, c)
