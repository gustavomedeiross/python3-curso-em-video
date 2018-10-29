s = 0
for c in range(1, 6):
    n = int(input('Digite um valor'))
    n1 = n % 2
    if n1 == 0:
        s += n
print('A soma de todos os números pares digitados é {}'.format(s))