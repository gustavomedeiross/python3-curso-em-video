alunos = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    alunos.append(aluno[:])
    alunos[cont].append(notas[:])
    aluno.clear()
    notas.clear()

    qrcnt = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if qrcnt not in 'SN':
        qrcnt = str(input('\033[31mInválido.\033[mQuer continuar? [S/N]')).upper().strip()[0]
    if qrcnt == 'N':
        break
print(alunos)