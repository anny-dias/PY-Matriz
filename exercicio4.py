'''Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, calcule o somatório dos 
elementos da diagonal principal da matriz'''

import random
def preencher(linha, coluna):
    #preencher a matriz
    matriz = []
    for i in range(linha):      # linha
        linha = []      
        for j in range(coluna):      # coluna
            n = random.randint(1,10)
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibir(matriz):
    # exibe a matriz
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
            print()

def soma_diagonal_principal(matriz):
    soma = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:          # indice de linha == indice de coluna
                soma += matriz[i][j]
    return soma