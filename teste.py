def criar_tabuleiro(n_linhas, n_colunas):
    """Cria e retorna a matriz do tabuleiro preenchida pelo usuário."""
    matriz = [] 
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = input(f"Linha {i}, Coluna {j} - Digite 💧 para vazio e 🚤 para navio: ")
            linha.append(n)
        matriz.append(linha)
    return matriz
 
def exibir_tabuleiro(matriz):
    """Exibe o tabuleiro de forma dinâmica e compreensível para o jogador."""
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    
    # Cabeçalho dinâmico das colunas
    cabecalho = "\n "
    for j in range(n_colunas):
        cabecalho += f" {j} "
    print(cabecalho)
    
    for i in range(n_linhas):
        linha_str = f"{i}"
        for j in range(n_colunas):
            linha_str += f"[{matriz[i][j]}]"
        print(linha_str)
    print()
 
def verificar_jogada(matriz, linha, coluna):
    """Valida as coordenadas e atualiza o estado do tabuleiro alvo conforme a jogada."""
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    
    if not (0 <= linha < n_linhas and 0 <= coluna < n_colunas):
        return False, "Coordenada inválida! Escolha números dentro dos limites do tabuleiro."

    posicao = matriz[linha][coluna]
    
    if posicao == '🚤':
        matriz[linha][coluna] = '💥'
        return True, "Acertou em cheio! 💥"
    elif posicao == '💧':
        matriz[linha][coluna] = '❌'
        return True, "Água! ❌"
    elif posicao == '💥' or posicao == '❌':
        return False, "Você já atirou nessa posição! Tente outra."
        
    return False, "Posição desconhecida."
 
def verificar_vitoria(matriz):
    """Verifica se ainda existem navios ('🚤') no tabuleiro."""
    for linha in matriz:
        for posicao in linha:
            if posicao == '🚤':
                return False
    return True
 
def trocar_jogador(jogador_atual):
    """Alterna o turno entre o Jogador 1 e o Jogador 2."""
    if jogador_atual == 1:
        return 2
    else:
        return 1
 
def main():
    """Função principal que controla o fluxo do jogo sem usar variáveis globais."""
    print("JOGADOR 1 - Monte seu tabuleiro:")
    jogador1 = criar_tabuleiro(5, 5)
    exibir_tabuleiro(jogador1)
 
    print("JOGADOR 2 - Monte seu tabuleiro:")
    jogador2 = criar_tabuleiro(5, 5)
    exibir_tabuleiro(jogador2)
 
    jogador_atual = 1
 
    while True:
        print(f"\nVez do Jogador {jogador_atual}")
 
        if jogador_atual == 1:
            matriz_alvo = jogador2
        else:
            matriz_alvo = jogador1
 
        # Loop para garantir que o jogador insira uma jogada válida
        while True:
            try:
                linha = int(input("Digite a linha que deseja atacar (0 a 4): "))
                coluna = int(input("Digite a coluna que deseja atacar (0 a 4): "))
            except ValueError:
                print("Por favor, digite apenas números inteiros válidos.")
                continue

            valido, mensagem = verificar_jogada(matriz_alvo, linha, coluna)
            print(mensagem)
            
            if valido:
                break # Sai do loop de tentativa se a jogada foi válida
 
        if verificar_vitoria(matriz_alvo):
            print(f"\nJogador {jogador_atual} venceu!")
            break
 
        jogador_atual = trocar_jogador(jogador_atual)
 
if __name__ == "__main__":
    main()