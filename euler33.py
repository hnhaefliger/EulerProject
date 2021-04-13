found = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            l = i / j
            m, n, o = str(i), str(j), str(k)

            if l < 1:
                if eval(m + o + '/' + n + o) == l:
                    found.append(m + o + '/' + n + o)

                if eval(m + o + '/' + o + n) == l:
                    found.append(m + o + '/' + o + n)

                if eval(o + m + '/' + n + o) == l:
                    found.append(o + m + '/' + n + o)

                if eval(o + m + '/' + o + n) == l:
                    found.append(o + m + '/' + o + n)

found = eval('(' + ')*('.join(found) + ')')
print(found)
