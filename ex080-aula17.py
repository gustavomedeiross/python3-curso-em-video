lista = []
for índice in range(0, 5):
   núm = int(input('Digite um número: '))
   if índice == 0 or núm > lista[-1]:
      lista.append(núm)
      print('Adicionado ao final da lista...')
   else:
       pos = 0
       while pos < len(lista):
           if núm <= lista[pos]:
               lista.insert(pos, núm)
               print(f'Adicionado na posição {pos} da lista...')
               break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
