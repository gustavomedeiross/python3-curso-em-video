qrcnt = 'S'
maior = menor = v1 = vu = 0
c = 0
while qrcnt == 'S':
    c += 1
    vu = v1
    v1 = int(input('===DIGITE UM VALOR==='))
    if v1 > maior:
        maior = v1
    else:
        menor = v1
    v1 += vu
    qrcnt = input('Você quer continuar? [S/N]').upper().strip()[0]

media = v1/c

print('O maior valor digitado foi {}, o menor foi {}, e a média de todos os valores é {}.'.format(maior, menor, media))
