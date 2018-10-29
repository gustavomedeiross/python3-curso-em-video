números = [[], []]
for c in range(1, 8):
   núm = int(input(f'Digite o {c}º valor: '))
   if núm % 2 == 0:
       números[0].append(núm)
   else:
       números[1].append(núm)
print(números)
números[0].sort()
números[1].sort()
print(f'Os números pares digitados foram {números[0]}')
print(f'Os números ímpares digitados foram {números[1]}')
