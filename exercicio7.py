'''Preencha uma matriz 5x4 com números informados pelo usuário e exiba a matriz. Em seguida, solicite 
um número e faça uma busca na matriz por esse número, informando a posição onde ele se encontra 
(índice da linha e índice da coluna). Se o número aparecer mais de uma vez na matriz, exiba todas as 
posições onde ele foi encontrado.'''

from modulo_matriz import preencher_matriz, exibe_matriz

matriz = preencher_matriz(5, 4)
exibe_matriz(matriz)

numero = int(input('Digite um valor: '))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == numero:
            print(f'Linha: {i} Coluna: {j}')