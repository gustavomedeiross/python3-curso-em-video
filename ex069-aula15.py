contde18 = contdehomens = contdemulheres20 = 0
while True:
   print('''===========================
   CADASTRE UMA PESSOA
===========================''')
   idade = int(input('Digite a idade da pessoa: '))
   sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
   while sexo not in 'MF':
       sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
   if idade > 18:
       contde18 += 1
   if sexo == 'M':
       contdehomens += 1
   if sexo == 'F' and idade < 20:
       contdemulheres20 += 1
   qrcntn = input('Cadastrar mais uma pessoa? [S/N]').upper().strip()[0]
   while qrcntn not in 'SN':
       qrcntn = input('Cadastrar mais uma pessoa? [s/n]').upper().strip()[0]
   if qrcntn == 'N':
       break
   else:
       print('Sexo inválido. Tente novamente.')
print(f'''DADOS REGISTRADOS:
Há {contde18} pessoas com mais de 18 anos.
Há {contdehomens} homens.
Há {contdemulheres20} mulheres com menos de 20 anos.''')