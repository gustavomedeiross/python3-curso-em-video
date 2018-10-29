n = no = int(input('Digite um número: '))
newn = 1
for c in range(n, 0, -1):
    newn *= c

print('O fatorial de {} é {}'.format(no, newn))