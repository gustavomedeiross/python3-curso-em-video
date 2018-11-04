n1 = float(input('Digite a sua primeira nota gafanhoto!'))
n2 = float(input('Digite a sua segunda nota gafanhoto!'))
m = (n1+n2)/2
if m < 5:
    print('Você foi \033[31mREPROVADO!\033[m')
elif m < 7:
    print('Você está em \033[33mrecuperação!\033[m')
elif m >= 7:
    print('Você foi \033[32maprovado!\033[m Muito bem!')
