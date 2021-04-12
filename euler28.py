i, j, s, k = 1, 2, 1, 0

while i < 1001**2:
    i += j
    s += i

    k += 1
    if k == 4:
        j += 2
        k = 0

print(s)
