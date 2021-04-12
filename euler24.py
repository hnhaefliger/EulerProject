digits = '0 1 2 3 4 5 6 7 8 9'.split()

def permute(root, available):
    if available:
        p = []

        for i in available:
            p += permute(root+i, [a for a in available if a != i])

        return p
        
    else:
        return [root]

permutations = sorted(permute('', digits))
