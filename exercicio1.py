'''Preencha uma matriz 3x5 com números inteiros informados pelo usuário e exiba a matriz.'''

matriz = []
for i in range(3):      # linha
    linha = []      
    for j in range(5):      # coluna
        n = int(input("Insira o número: "))
        linha.append(n)
    matriz.append(linha)
print(matriz)