def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}m x {comp}m é de {a}m²')


#Programa principal
print('CONTROLE DE TERRENOS')
print('=' * 30)
área(float(input('Digite a largura do terreno (m): ')), float(input('Digite o comprimento do terreno (m): ')))
