'''6. Implemente um jogo da velha entre 2 jogadores. Utilize uma matriz 3x3 como tabuleiro. A cada rodada, a 
matriz deve ser exibida no terminal exibindo o estado atual do jogo. A cada rodada um dos jogadores deve 
selecionar a posição que deseja marcar (X ou O).'''

from modulo_matriz import exibe_matriz

def validar_posicao(linha, coluna):
    if linha >=0 and linha <=2 and coluna >= 0 and coluna <= 2 and matriz[linha][coluna] == '-':
        return True
    else:
        return False
    
def empatou():
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == '-':
                return False
    return True

def ganhou(jogador):
    if matriz[0][0] == jogador and matriz[0][1] == jogador and matriz [0][2] == jogador or \
    matriz[1][0] == jogador and matriz[1][1] == jogador and matriz [1][2] == jogador or \
    matriz[2][0] == jogador and matriz[2][1] == jogador and matriz [2][2] == jogador or \
    matriz[0][0] == jogador and matriz[1][0] == jogador and matriz [2][0] == jogador or \
    matriz[0][1] == jogador and matriz[1][1] == jogador and matriz [2][1] == jogador or \
    matriz[0][2] == jogador and matriz[1][2] == jogador and matriz [2][2] == jogador or \
    matriz[0][0] == jogador and matriz[1][1] == jogador and matriz [2][2] == jogador or \
    matriz[0][2] == jogador and matriz[1][1] == jogador and matriz [2][0] == jogador :
        return True
    else:
        return False

    


matriz = [['-','-','-'],
          ['-','-','-'],
          ['-','-','-']]

jogador = 'X'
continuar = True

while continuar == True:
    exibe_matriz(matriz)
    print(f'JOGADOR {jogador}')
    linha = int(input('Selecione a linha: '))
    coluna = int(input('Selecione a coluna: '))

    if validar_posicao(linha, coluna):
        matriz[linha][coluna] = jogador
        if empatou():
            print('O jogo empatou')
            continuar = False
        if ganhou(jogador):
            print(f'o {jogador} venceu')
            continuar = False
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('Posição Inválida. Escolha novamente')

