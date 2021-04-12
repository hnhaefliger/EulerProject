digits = '1 2 3 4 5 6 7 8 9'.split()

def permute(root, options):
    permutations = []
    
    if options:
        for option in options:
            permutations += permute(root + option, [o for o in options if o != option])

        return permutations

    else:
        return [root]

permutations = permute('', digits)
found = []

for permutation in permutations:
    for i in range(1, 8):
        for j in range(i+1, 9):
            if int(permutation[:i]) * int(permutation[i:j]) == int(permutation[j:]):
                if int(permutation[j:]) not in found:
                    found.append(int(permutation[j:]))

print(sum(found))

            
