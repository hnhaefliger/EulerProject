def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

a, b, c = 285, 165, 143
x, y, z = 0, 0, 0

while not(x == y == x) or x == 0 or x == 1:
    c += 1
    z = hexagonal(c)

    while z > y:
        b += 1
        y = pentagonal(b)

    while z > x:
        a += 1
        x = triangle(a)

print(a, b, c, x, y, z)
