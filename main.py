#Criação do tabuleiro
def tabuleiro1(n_linhas, n_colunas):
    matriz = [] 
 
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = input('Digite 💧 para espaços vazios, e 🚤 para navios: ')
            linha.append(n)
        matriz.append(linha)
    return matriz
#Organização da matriz e orientação de indice
def exibir_tabuleiro(matriz):
    print("\n 0  1  2  3  4 ")
    for i in range (5):
        linha = f'{i}'
        for j in range(5):
            linha += f"[{matriz[i][j]}]"
        print(linha)
    print()

#Verificação de jogada/Validação de limites e acertos 
def verificar_jogada(matriz, linha, coluna):
    if (linha > 4 and coluna < 0):
        return "Coordenada inválida! Escolha números entre 0 e 4."
    
    posicao = matriz[linha][coluna]
    
    if posicao == '🚤':
        matriz[linha][coluna] = '💥'
        return "Acertou em cheio! 💥"
    
    elif posicao == '💧':
        matriz[linha][coluna] = '❌'
        return "Água! ❌"
        
    elif posicao == '💥' or posicao == '❌':
        return "Você já atirou nessa posição! Tente outra."
        
    return "Posição desconhecida."


def verificar_vitoria(matriz):
    for linha in matriz:
        for posicao in linha:
            if posicao == '🚤':
                return False

    return True


def trocar_jogador(jogador_atual):
    if jogador_atual == 1:
        return 2
    else:
        return 1


print("JOGADOR 1 - Monte seu tabuleiro:")
jogador1 = tabuleiro1(5, 5)
exibir_tabuleiro(jogador1)

print("JOGADOR 2 - Monte seu tabuleiro:")
jogador2 = tabuleiro1(5, 5)
exibir_tabuleiro(jogador2)

jogador_atual = 1

while True:
    print(f"\nVez do Jogador {jogador_atual}")

    if jogador_atual == 1:
        matriz_alvo = jogador2
    else:
        matriz_alvo = jogador1

    linha = int(input("Digite a linha que deseja atacar (0 a 4): "))
    coluna = int(input("Digite a coluna que deseja atacar (0 a 4): "))

    resultado = verificar_jogada(matriz_alvo, linha, coluna)
    print(resultado)

    if verificar_vitoria(matriz_alvo):
        print(f"\nJogador {jogador_atual} venceu!")
        break

    jogador_atual = trocar_jogador(jogador_atual)   