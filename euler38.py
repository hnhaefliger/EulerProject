def pandigital(n):
    if '0' in n:
        return False
    
    for i in range(1, 10):
        if n.count(str(i)) != 1:
            return False

    return True

m = [0, 0, 0]

for n in range(2, 10):
    for i in range(10000):
        c = ''
        
        for j in range(n):
            c += str((1+j)*i)

        if pandigital(c) and int(c) > m[2]:
            m = [n, i, int(c)]

print(m)
            
    
