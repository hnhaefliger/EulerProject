def fact(n):
    f = 1
    
    for i in range(1, n+1):
        f = f*i

    return f

found = []

for i in range(3, 100000):
    if i == sum([fact(int(j)) for j in str(i)]):
        print(i)
        found.append(i)

print(sum(found))
