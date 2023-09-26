'''1. Preencha uma matriz 5x5 com números aleatórios (de 1 a 25), de forma que nenhum número se repita na 
matriz, ou seja, caso o número sorteado já esteja contido na matriz, outro número deve ser sorteado.
'''

from modulo_matriz import preencher_matriz_aleatoria_diferente, exibe_matriz

 
matriz = preencher_matriz_aleatoria_diferente(5, 5)
exibe_matriz(matriz)