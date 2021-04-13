def pandigital(i):
    i = str(i)
    n = len(i)
    n = [str(j) for j in range(0, n)]

    if all([j in n for j in i]) and all([i.count(j) == 1 for j in n]):
        return True
    
    else:
        return False

def properties(n):
    n = str(n)

    if int(n[1:4]) % 2 == 0:
        if int(n[2:5]) % 3 == 0:
            if int(n[3:6]) % 5 == 0:
                if int(n[4:7]) % 7 == 0:
                    if int(n[5:8]) % 11 == 0:
                        if int(n[6:9]) % 13 == 0:
                            if int(n[7:]) % 17 == 0:
                                return True

    return False

found = []

for i in range(1023456789, 9876543211):
    if properties(i):
        if pandigital(i):
            print(i)
            found.append(i)

print(sum(found))
