'''Preencha uma matriz 10x10 com números aleatórios e exiba a matriz. A seguir, exiba o somatório dos 
elementos da diagonal secundária da matriz'''

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

            if i + j == len(matriz)-1:      # soma do indice de linha e coluna == tamanho -1

                soma += matriz[i][j]    

    return soma