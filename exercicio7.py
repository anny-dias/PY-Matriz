'''Preencha uma matriz 5x4 com números informados pelo usuário e exiba a matriz. Em seguida, solicite 
um número e faça uma busca na matriz por esse número, informando a posição onde ele se encontra 
(índice da linha e índice da coluna). Se o número aparecer mais de uma vez na matriz, exiba todas as 
posições onde ele foi encontrado.'''

matriz = []
for i in range(5):      # linha
    lista = []      
    for j in range(4):      # coluna
        n = int(input("Insira o número: "))
        lista.append(n)
    matriz.append(lista)