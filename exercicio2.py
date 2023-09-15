'''Preencha uma matriz 6x6 com o elemento 1 em todas as posições em que o índice de linha tem valor 
igual ao índice da coluna. Preencha os demais elementos com zero e exiba a matriz.'''

linha = 6
coluna = 6

matriz = []
for linhas in range(linha):
    lista = []
    for colunas in range(coluna):
        n = int(input("Insira o número: "))
        lista.append(n)
    matriz.append(lista)
print(matriz)

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if matriz[linha] == matriz[coluna]:
            matriz[linha][coluna] = 1