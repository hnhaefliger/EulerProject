import math

def isprime(n):
    n = int(n)
    
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True
            
found = []
i = 10

while len(found) < 11:
    s = str(i)

    if isprime(i):
        for j in range(1, len(s)):
            if not(isprime(s[j:]) and isprime(s[:-j])):
                break

        else:
            found.append(i)

    i += 1

print(found, sum(found))
