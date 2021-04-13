i = 0
constant = ''

while len(constant) < 1000001:
    constant += str(i)
    i += 1

print(int(constant[1]) * int(constant[10]) * int(constant[100]) * int(constant[1000]) * int(constant[10000]) * int(constant[100000]) * int(constant[1000000]))
