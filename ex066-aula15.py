n = cont = sum = 0
while True:
   n = int(input('Digite um número (para parar digite 999)'))
   if n == 999:
       break
   sum += n
   cont += 1
print(f'A soma dos números é {sum} e a quantidade de números digitados foi {cont}')

