def binary(n):
    highest = 0

    while 2**highest < n:
        highest += 1

    b = ''
    
    for i in range(highest, -1, -1):
        if n - 2**i >= 0:
            n -= 2**i
            b += '1'

        else:
            b += '0'

    if b[0] == '0':
        b = b[1:]

    return b
            
found = []

for i in range(1000000):
    if str(i) == str(i)[::-1]:
        b = binary(i)
        if b == b[::-1]:
            found.append(i)

print(found, sum(found))
