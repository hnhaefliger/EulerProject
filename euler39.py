import math

m = [0, 0]

for p in range(0, 1001):
    s = 0
    
    for a in range(p):
        for b in range(a, p):
            c = p - a - b
            
            if a**2 + b**2 == c**2:
                s += 1

    if s > m[0]:
        m = [s, p]

print(m)
