n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla = (n1, n2, n3, n4)
tupla2 = (n1 % 2, n2 % 2, n3 % 2, n4 % 2)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for pos, x in enumerate(tupla2):
    if x == 0:
        print(tupla[pos], end=' ')
