i = 2

found = []

while True:
    s = 0
    for digit in str(i):
        s += int(digit)**5

    if s == i:
        found.append(i)

    i += 1
