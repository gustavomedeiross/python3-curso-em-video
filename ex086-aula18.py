matriz = [[], [], []]
for pos in range(0, len(matriz)):
   for c in range(0, 3):
       núm = int(input(f'Digite um valor para [{pos}, {c}]: '))
       matriz[pos].append(núm)
print('=' * 30)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')