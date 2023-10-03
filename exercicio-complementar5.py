'''5. Uma matriz quadrada é chamada de "quadrado mágico" se a soma dos elementos de cada linha, cada coluna 
e a soma dos elementos das diagonais principal e secundária são todos iguais. Escreva um programa que 
preencha uma matriz 4x4 com valores informados pelo usuário e informe se ela é ou não um quadrado 
mágico. 
Exemplo: a matriz abaixo é um quadrado mágico.
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
'''

from modulo_matriz import preencher_matriz, exibe_matriz

matriz = preencher_matriz(4, 4)
exibe_matriz(matriz)

lista_somas = []

#soma das linhas
for i in range(len(matriz)):
    s = 0       #somadora
    for j in range(len(matriz[0])):
        s += matriz[i][j]
    lista_somas.append(s)

#soma das colunas
for i in range(len(matriz)):
    s = 0
    for j in range(len(matriz[0])):
        s += matriz[j][i]
    lista_somas.append(s)

#soma das diagonais
soma_diagonal = 0
soma_secundaria = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:                          #diagonal principal
            soma_diagonal += matriz[i][j]
        if i + j == len(matriz) - 1:        #diagonal secundaria
            soma_secundaria += matriz[i][j]
    lista_somas.append(soma_diagonal)
    lista_somas.append(soma_secundaria)

print(lista_somas)
lista_somas = set(lista_somas)              #copia para o conjunto
print(lista_somas)

if len(lista_somas) == 0:
    print('Quadrado mágico')
else:
    print('Não é um Quadrado mágico')





