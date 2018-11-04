#fórmula = |b-c| < a < b + c
r1 = int(input('Digite o tamanho da reta 1 = '))
r2 = int(input('Digite o tamanho da reta 2 = '))
r3 = int(input('Digite o tamanho da reta 3 = '))
#abs = comando que basicamente "modula",
# ou seja, sempre transforma um número em positivo
if abs(r2-r3) < r1 < r2 + r3:
    print('Esse triângulo pode ser feito!')
    if r1 == r2 == r3:
        print('Esse é um triângulo equilátero!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2==r3 != r1:
        print('Esse triâgulo é isósceles!')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é escaleno!')
else:
    print('Esse triângulo não pode ser feito!')
