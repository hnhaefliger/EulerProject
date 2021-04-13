import math

def isprime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def rotate(string):
    return string[-1] + string[:-1]

found = []

for i in range(1, 1000000):
    string = str(i)
    
    for j in range(len(str(i)) + 1):
        if not(isprime(int(string))):
            break
        
        string = rotate(string)

    else:
        found.append(i)

print(found, len(found))
