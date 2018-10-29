print('Digite 2 valores!')
v1 = float(input('Valor 1 ='))
v2 = float(input('Valor 2 ='))

txt ='''Escolha qual operação você quer fazer:
[1] -> Somar
[2] -> Multiplicar
[3] -> Maior
[4] -> Novos Números
[5] -> Sair do Programa'''

menu = int(input(txt))

while menu != 5:
    if menu == 1:
        print('A soma entre os valores {} e {} é {}'.format(v1, v2, v1+v2))
    elif menu == 2:
        print('A multiplicação entre os valores {} e {} é {}'.format(v1, v2, v1*v2))
    elif menu == 3:
        if v1 > v2:
            print('O maior número entre os dois é {}'.format(v1))
        else:
            print('O maior número entre os dois é {}'.format(v2))
    elif menu == 4:
        v1 = float(input('Novo Valor 1 ='))
        v2 = float(input('Novo Valor 2 ='))
    else:
        menu = int(input('Número inválido. Digite novamente'))
    menu = int(input(txt))
print('Obrigado por participar do programa!')
