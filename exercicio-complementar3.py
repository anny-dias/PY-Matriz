'''3. Faça um programa que preenche uma matriz 7x7 com números aleatórios e gere uma lista de 7 elementos 
que contenha o maior elemento de cada uma das linhas da matriz.
'''

from modulo_matriz import preencher_matriz_aleatoria, exibe_matriz

matriz = preencher_matriz_aleatoria(7, 7)
exibe_matriz(matriz)

menor = matriz[0][0] 
linha = 0
coluna = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > menor:
            menor = matriz[i][j]
            linha = i
            coluna = j
print(f'O menor valor é {menor} e está na linha {linha} e coluna {coluna}')
