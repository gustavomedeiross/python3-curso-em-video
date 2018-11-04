n1 = int(input('Digite um primeiro termo de uma P.A. ='))
r = int(input('Digite a razão de uma P.A. = '))
ndt = (n1 + r*10)
for c in range(n1, ndt,  r):
    print(c, end='...')
