'''4. Preencha uma matriz 6x6 com números aleatórios e multiplique cada elemento da matriz pelo maior 
elemento de sua linha. Escrever a matriz original e a modificada'''

from modulo_matriz import preencher_matriz_aleatoria, exibe_matriz

matriz = preencher_matriz_aleatoria(4, 4)
exibe_matriz(matriz)

maiores = []

for i in range(len(matriz)):
    maior = 0
    for j in range(len(matriz[0])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    maiores.append(maior)

    for j in range(len(matriz[0])):
        matriz[i][j] *= maior

print(maiores)
exibe_matriz(matriz)
