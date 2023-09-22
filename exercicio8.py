'''Preencha uma matriz 4x4 com números informados pelo usuário e exiba a matriz. Na sequência, gere 
a transposta da matriz e exiba-a (matriz transposta é a matriz que se obtém da troca de linhas por 
colunas da matriz)'''

from modulo_matriz import preencher_matriz, exibe_matriz

matriz = preencher_matriz(4, 4)
exibe_matriz(matriz)

transposta = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[0])):
        linha.append(matriz[j][i])
    transposta.append(linha)
exibe_matriz(transposta)