#ele queria que mostrasse a posição de mais de um (caso fossem dois valores - maior e menor- iguais)
#por isso tive que fazer uma leve alteração

lista = list()
maior = menor = 0
for pos in range(0, 5):
   lista.append(int(input(f'Digite um valor para a posição {pos}: ')))
   if pos == 0:
       maior = menor = lista[pos]
   else:
       if lista[pos] > maior:
           maior = lista[pos]

       if lista[pos] < menor:
           menor = lista[pos]
print('-=' * 30)
print(f'Os valores digitados foram {lista}')

print(f'O maior valor digitado foi {maior}, que está nas posições', end=' ')
for posmaior, valor in enumerate(lista):
   if valor == maior:
       print(f'{posmaior}...', end='')
print()
print(f'O menor valor digitado foi {menor}, que está na posição', end=' ')
for posmenor, valor in enumerate(lista):
   if valor == menor:
       print(f'{posmenor}...', end='')
print()
