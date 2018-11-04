s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor'))
    n1 = n % 2
    if n1 == 0:
        s += n
print('A soma de todos os números pares digitados é {}'.format(s))
