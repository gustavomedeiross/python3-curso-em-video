n1 = int(input('Digite um número ='))
s = 0
for c in range(2, n1):
    if n1 % c  == 0:
        s += 1

if s >= 1:
    print('O número {} não é um número primo'.format(n1))
else:
    print('O número {} é um número primo'.format(n1))

print('{:=^21}'.format('FIM'))

