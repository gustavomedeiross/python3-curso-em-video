print('''==========================
       BANCO GMM
==========================''')
cedulasde50 = cedulasde20 = cedulasde10 = cedulasde1 = 0
saque = int(input('Quanto você quer sacar? R$'))

while True:
   if saque >= 50:
       cedulasde50 += 1
       saque -= 50
   else:
       break
while True:
   if saque >= 20:
       cedulasde20 += 1
       saque -= 20
   else:
       break
while True:
   if saque >= 10:
       cedulasde10 += 1
       saque -= 10
   else:
       break
while True:
   if saque >= 1:
       cedulasde1 += 1
       saque -= 1
   else:
       break


print(f'''Total de {cedulasde50} cédulas de R$50,00
Total de {cedulasde20} cédulas de R$20,00
Total de {cedulasde10} cédulas de R$10,00
Total de {cedulasde1} cédulas de R$1,00''')
