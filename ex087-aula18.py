matriz = [[], [], []]
par = tercoluna = maiorvalor = 0

for pos in range(0, len(matriz)):
   for c in range(0, 3):
       núm = int(input(f'Digite um valor para [{pos}, {c}]: '))
       matriz[pos].append(núm)
       if núm % 2 == 0:
           par += núm
       if c == 2:
           tercoluna += núm
       if pos == 1:
           if c == 0:
               maiorvalor = núm
           else:
               if núm > maiorvalor:
                   maiorvalor = núm

print('=' * 30)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')
print('=' * 30)
#segunda parte - exercício 87
print(f'A soma de todos os números pares é {par}')
print(f'A soma da terceira coluna é {tercoluna}')
print(f'O maior valor da segunda linha é {maiorvalor}')
