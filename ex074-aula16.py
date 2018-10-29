from random import choices
núm = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n1 = choices(núm, k=5)
menor = maior = n1[0]
for c in n1:
    if c < menor:
        menor = c
    if c > maior:
        maior = c

print(n1[0], n1[1], n1[2], n1[3], n1[4])
print(f'O menor número da lista é o {menor}')
print(f'O maior número da lista é o {maior}')