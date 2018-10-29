s = 0
for c in range(3, 500+1, 6):
    s += c
print('''A soma de todos os números entre 1 e 500, 
que são ímpares e múltiplos de 3 é {}!'''.format(s))