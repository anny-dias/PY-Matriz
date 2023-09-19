'''Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, informe o menor 
elemento da matriz.'''

matriz = []
for i in range(5):      # linha
    lista = []      
    for j in range(5):      # coluna
        n = int(input("Insira o número: "))
        lista.append(n)
    matriz.append(lista)