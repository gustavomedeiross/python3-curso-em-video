import emoji
frase = input('Digite uma frase: ')
frase = frase.split()
frase = ''.join(frase)
inverso = ''

for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]
if frase == inverso:
    print(emoji.emojize('Essa frase é um palíndromo :thumbs_up:'))
if frase != inverso:
    print(emoji.emojize('Essa frase não é um palíndromo :crying_cat_face:'))
