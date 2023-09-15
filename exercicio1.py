'''Preencha uma matriz 3x5 com números inteiros informados pelo usuário e exiba a matriz.'''

linha = 3
coluna = 5

matriz = []
for linhas in range(linha):
    lista = []
    for colunas in range(coluna):
        n = int(input("Insira o número: "))
        lista.append(n)
    matriz.append(lista)
print(matriz)