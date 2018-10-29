import emoji
frase = input('Digite uma frase: ')
frase = frase.split()
frase = ''.join(frase)
numdc = len(frase)

for c1 in range(0, numdc):
    v1 = frase[c1]
for c2 in range(numdc-1, -1, -1):
    v2 = frase[c2]
if v1 == v2:
    print(emoji.emojize('Essa frase é um palíndromo :thumbs_up:'))
if v1 != v2:
    print(emoji.emojize('Essa frase não é um palíndromo :crying_cat_face:'))