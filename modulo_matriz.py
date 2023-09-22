from random import randint
def preencher_matriz(lin: int, col: int) -> list:
    '''Preenche a matriz com entrada do usuário'''
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = int(input('Numero: '))
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibe_matriz(matriz: list) -> None:
    '''Imprime a matriz'''
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()

def preencher_matriz_aleatoria(lin: int, col: int) -> list:
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = randint(1, 50)
            linha.append(n)
        matriz.append(linha)
    return matriz



