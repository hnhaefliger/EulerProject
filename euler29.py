values = []

for a in range(2, 101):
    for b in range(2, 101):
        c = a**b
        if c not in values:
            values.append(c)

print(len(values))
