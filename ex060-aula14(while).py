n = no = int(input('Digite um valor: '))
n += 1
newn = 1
while n > 1:
    n -= 1
    newn *= n

print('O fatorial do número {} é {}'.format(no, newn))
