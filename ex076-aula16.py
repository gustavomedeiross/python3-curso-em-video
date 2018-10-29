listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Penal', 25.00, 'Transferidor', 4.2, 'Compasso', 9.99,
          'Mochila', 120.32, 'Caneta', 2.00, 'Livro', 34.9)


print(f'''{'-' * 42}
            LISTAGEM DE PREÇOS
{'-' * 42}''')


for x in range(0, len(listagem)):
    if x % 2 == 0:
        qdp = 31 - (len(listagem[x]))
        print(listagem[x], '.' * (qdp), end='R$')
    if x % 2 != 0:
        if listagem[x] < 10:
            print('{}{:.2f}'.format(' ' * 3, listagem[x]))
        elif listagem[x] >= 10 and listagem[x] < 100:
            print('{}{:.2f}'.format(' ' * 2, listagem[x]))
        elif listagem[x] >= 100 and listagem[x] < 1000:
            print('{}{:.2f}'.format(' ', listagem[x]))
        elif listagem[x] >= 1000:
            print('{:.2f}'.format(listagem[x]))
print('-' * 42)