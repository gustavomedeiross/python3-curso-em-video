números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


n = int(input('Digite um número!'))
while n < 0 or n > 20:
    n = int(input('Erro. Digite novamente'))
print(f'Você digitou o número {números[n]}')
