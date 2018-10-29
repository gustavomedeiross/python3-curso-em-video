n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal''')
opção = int(input('Sua opção = '))
if opção == 1:
    print('O número {} convertido para binário é {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('O número {} convertido para octal é {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('O número digitado é inválido!')