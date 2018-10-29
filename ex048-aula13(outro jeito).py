s = 0
for c in range(3, 501, 2):
    n = c % 3
    if n == 0:
        s += n
print('''A soma de todos os números ímpares e 
múltiplos de 3 entre 1 e 500 é {}!'''.format(s))