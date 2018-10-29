#faça um programa que leia algo pelo teclado e
#mostre na tela o seu tipo primitivo e todas as
#informações possíveis sobre ele.
rand = input('Digite algo!')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'branco': '\033[30m'}

print('{}É uma letra? =', rand.isalpha(), '{}\n'.format(cores['verde'], cores['limpa']))
print('{}É um número? =', rand.isnumeric(), '{}\n'.format(cores['amarelo'], cores['limpa']))
print('{}É alfanumérico? =', rand.isalnum(), '{}\n'.format(cores['azul'], cores['limpa']))
print('{}É decimal? =', rand.isdecimal(), '{}\n'.format(cores['branco'], cores['limpa']))
print('{}É um digito? =', rand.isdigit(), '{}\n'.format(cores['branco'], cores['limpa']))
print('{}É maiúsculo? =', rand.isupper(), '{}\n'.format(cores['azul'], cores['limpa']))
print('{}É minúsculo? =', rand.islower(), '{}\n'.format(cores,['amarelo'], cores['limpa']))
print('{}É printable? =', rand.isprintable(), '{}'.format(cores['verde'], cores['limpa']))