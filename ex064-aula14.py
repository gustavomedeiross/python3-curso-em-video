número = soma = cont = 0
número = int(input('Digite um número qualquer, e se quiser parar o programa digite 999'))
while número != 999:
    cont += 1
    soma += número
    número = int(input('Digite um número qualquer, e se quiser parar o programa digite 999'))

print(f'''Números digitados = {cont}. 
Soma de todos = {soma}.''')
