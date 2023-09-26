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
    '''Preenche a matriz com números aleatorios'''
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = randint(1, 50)
            linha.append(n)
        matriz.append(linha)
    return matriz

def preencher_matriz_aleatoria_diferente(lin: int, col: int) -> list:
    '''Preenche a matriz com números aleatorios difrentes'''
    matriz = []
    sorteados = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = randint(1, 25)
            while n in sorteados:
                n = randint(1, 25)
            linha.append(n)
            sorteados.append(n)
        matriz.append(linha)
    return matriz



