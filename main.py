def tabuleiro1(n_linhas, n_colunas):
    matriz = [] 
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = input('Digite 💧 para espaços vazios, e 🚤 para navios: ')
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibir_tabuleiro(matriz):
    print("\n 0  1  2  3  4 ")
    for i in range (5):
        linha = f'{i}'
        for j in range(5):
            linha += f"[{matriz[i][j]}]"
        print(linha)
    print()

def verificar_jogada(matriz, linha, coluna):
    if not (0 <= linha < 5 and 0 <= coluna < 5):
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

jogador1 = tabuleiro1(5,5) 
tabu = exibir_tabuleiro(jogador1)