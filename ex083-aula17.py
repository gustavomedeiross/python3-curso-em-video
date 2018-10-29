expressão = str(input('Digite uma expressão: '))
lista = []
for símb in expressão:
   if símb == '(':
       lista.append('(')
   elif símb == ')':
       if len(lista) > 0:
           lista.pop()
       else:
           lista.append(')')
           break

if len(lista) == 0:
   print('A sua expressão é válida!')
else:
   print('A sua expressão é inválida!')
