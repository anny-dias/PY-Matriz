'''Preencha uma matriz 4x4 com números informados pelo usuário e exiba a matriz. Na sequência, gere 
a transposta da matriz e exiba-a (matriz transposta é a matriz que se obtém da troca de linhas por 
colunas da matriz)'''

matriz = []
for i in range(4):      # linha
    lista = []      
    for j in range(4):      # coluna
        n = int(input("Insira o número: "))
        lista.append(n)
    matriz.append(lista)