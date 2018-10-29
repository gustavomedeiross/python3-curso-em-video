#fórmula = |b-c| < a < b + c
r1 = int(input('Digite o tamanho da reta 1 = '))
r2 = int(input('Digite o tamanho da reta 2 = '))
r3 = int(input('Digite o tamanho da reta 3 = '))
#abs = comando que basicamente "modula",
# ou seja, sempre transforma um número em positivo
if abs(r2-r3) < r1 < r2 + r3:
else:
    print('Esse triângulo não pode ser feito!')
