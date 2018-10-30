from time import sleep
alunos = []
aluno = []
notas = []
cont = 0

while True:
    aluno.append(str(input('Nome: ')).capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    aluno.append(cont) #número do aluno

    aluno.append((notas[0] + notas[1]) / 2) #média

    aluno.append(notas[:])
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()

    cont += 1

    qrcnt = input('Quer continuar? [S/N]').upper().strip()[0]
    if qrcnt not in 'SN':
        qrcnt = str(input('\033[31mInválido.\033[mQuer continuar? [S/N]')).upper().strip()[0]
    if qrcnt == 'N':
        break

print('=' * 30)
print(f'{"No.":<6}{"NOME":<12}{"MÉDIA":10}')
print('-' * 30)
for c in range(0, len(alunos)):
    print(f'{alunos[c][1]:<6}{alunos[c][0]:<12}{alunos[c][2]:<10.2f}')
print('-' * 30)
#-------------------
while True:
    mostrar = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    for x in range(0, len(alunos)):
        if alunos[x][1] == mostrar:
            print(f'Notas de {alunos[x][0]} são {alunos[x][3]}')
            print('-' * 30)
    if mostrar == 999:
        print('FINALIZANDO...')
        break
sleep(1)
print('<<< VOLTE SEMPRE >>>')

