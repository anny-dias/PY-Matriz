'''Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, informe o menor 
elemento da matriz.'''
from modulo_matriz import preencher_matriz_aleatoria, exibe_matriz

matriz = preencher_matriz_aleatoria(5, 5)
exibe_matriz(matriz)

menor = matriz[0][0] 
linha = 0
coluna = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha = i
            coluna = j
print(f'O menor valor é {menor} e está na linha {linha} e coluna {coluna}')
