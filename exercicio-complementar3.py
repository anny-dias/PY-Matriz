'''3. Faça um programa que preenche uma matriz 7x7 com números aleatórios e gere uma lista de 7 elementos 
que contenha o maior elemento de cada uma das linhas da matriz.
'''


from modulo_matriz import preencher_matriz_aleatoria, exibe_matriz

matriz = preencher_matriz_aleatoria(7, 7)
exibe_matriz(matriz)

maiores = []

for i in range(len(matriz)):
    maior = 0
    for j in range(len(matriz[0])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    maiores.append(maior)

print(maiores)

