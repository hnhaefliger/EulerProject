import math

def composite(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return True

    return False

def prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

i = 1

while True:
    i += 2

    if composite(i):
        for j in range(i):
            if prime(j):
                d = i - j
                s = math.sqrt(d / 2)

                if int(s) == s:
                    break

        else:
            print(i)
