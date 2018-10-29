n1 = int(input('Digite o primeiro de uma P.A. = '))
r = int(input('Digite a razão da P.A. = '))
ndt = (n1 + r*10)
while n1 != ndt:
    print(n1)
    n1 += r

#------------------------------------------#

extra = int(input('Estes são os 10 primeiros termos da P.A. Quantos temos mais você quer mostrar?'))
newndt = (n1 + r*extra)
while extra != 0:

    while n1 != newndt:
        print(n1)
        n1 += r
    extra = int(input('Quantos termos mais você quer mostrar?'))
    newndt = (n1 + r * extra)

print('Obrigado por utilizar o programa!')