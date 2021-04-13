alphabet = '" a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

def word_value(word):
    return sum([alphabet.index(letter) for letter in word])

with open('words.txt', 'r') as f:
    words = f.read().lower().replace('"', '').split(',')

    values = [word_value(word) for word in words]

    i = 1
    triangles = [-1]

    while triangles[-1] < max(values):
        triangles.append(0.5 * i * (i+1))
        i += 1

    valid = [value for value in values if value in triangles]

print(len(valid))
