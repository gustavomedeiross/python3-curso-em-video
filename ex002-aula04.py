#Crie um script de python que leia o dia, o mês e
#o ano de nascimento de uma pessoa e mostre uma
#mensagem com a data formatada.
d = input('\033[4;30;41mQue dia você nasceu?\033[m')
m = input('\033[4;31mQue mês você nasceu?\033[m')
a = input('\033[4;31;47mQue ano você nasceu?\033[m')
print('\033[41;37;4mVocê nasceu dia {}/{}/{}.\033[m'.format(d, m, a))