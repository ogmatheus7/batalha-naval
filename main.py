def criar_tabuleiro(n_linhas, n_colunas):
    matriz = []

    for i in range(n_linhas):
        linha = []

        for j in range(n_colunas):
            linha.append('💧')

        matriz.append(linha)

    return matriz


def posicionar_navios(matriz, quantidade):
    navios_colocados = 0

    while navios_colocados < quantidade:
        try:
            letra = input("Digite a linha do navio (A a E): ").upper()
            linha = converter_linha(letra)
            coluna = int(input("Digite a coluna do navio (0 a 4): "))
        except ValueError:
            print("Digite uma coluna válida!")
            continue

        if linha == -1 or not (0 <= coluna < 5):
            print("Coordenada inválida! Escolha uma linha de A a E e uma coluna de 0 a 4.")

        elif matriz[linha][coluna] == '🚤':
            print("Já existe um navio nessa posição! Escolha outra.")

        else:
            matriz[linha][coluna] = '🚤'
            navios_colocados += 1

    return matriz


def exibir_tabuleiro(matriz):
    print("\n    0    1    2    3    4")

    letras = ['A', 'B', 'C', 'D', 'E']

    for i in range(5):
        linha = f'{letras[i]}'

        for j in range(5):
            linha += f" [{matriz[i][j]}]"

        print(linha)

    print()


def exibir_tabuleiro_ataque(matriz):
    print("\n    0    1    2    3    4")

    letras = ['A', 'B', 'C', 'D', 'E']

    for i in range(5):
        linha = f'{letras[i]}'

        for j in range(5):
            if matriz[i][j] == '🚤':
                linha += ' [💧]'
            else:
                linha += f' [{matriz[i][j]}]'

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


def iniciar_jogo():
    print("JOGADOR 1 - Monte seu tabuleiro:")
    jogador1 = criar_tabuleiro(5, 5)
    posicionar_navios(jogador1, 3)
    exibir_tabuleiro(jogador1)

    print("JOGADOR 2 - Monte seu tabuleiro:")
    jogador2 = criar_tabuleiro(5, 5)
    posicionar_navios(jogador2, 3)
    exibir_tabuleiro(jogador2)

    jogador_atual = 1
    radar_jogador1 = True
    radar_jogador2 = True

    while True:
        print(f"\nVez do Jogador {jogador_atual}")

        if jogador_atual == 1:
            matriz_alvo = jogador2
        else:
            matriz_alvo = jogador1

        exibir_tabuleiro_ataque(matriz_alvo)
        print("1 - Atacar")
        print("2 - Usar radar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                letra = input("Digite a linha que deseja atacar (A a E): ").upper()
                linha = converter_linha(letra)
                coluna = int(input("Digite a coluna que deseja atacar (0 a 4): "))
            except ValueError:
                print("Digite uma coluna válida!")
                continue
            if linha == -1:
                print("Linha inválida! Escolha uma letra de A a E.")
                continue

            resultado = verificar_jogada(matriz_alvo, linha, coluna)
            print(resultado)

            if resultado == "Você já atirou nessa posição! Tente outra." or resultado == "Coordenada inválida! Escolha números entre 0 e 4.":
                continue

            if verificar_vitoria(matriz_alvo):
                print(f"\nJogador {jogador_atual} venceu!")
                break
            jogador_atual = trocar_jogador(jogador_atual)

        elif opcao == "2":
            if jogador_atual == 1 and radar_jogador1 == False:
                print("Jogador 1 já utilizou o radar!")
                continue

            if jogador_atual == 2 and radar_jogador2 == False:
                print("Jogador 2 já utilizou o radar!")
                continue
            letra = input("Digite a linha que deseja escanear (A a E): ").upper()
            linha = converter_linha(letra)

            if linha == -1:
                print("Linha inválida! Escolha uma letra de A a E.")
                continue

            if usar_radar(matriz_alvo, linha):
                print(f"📡 Radar detectou um navio na linha {letra}!")
            else:
                print(f"📡 Nenhum navio detectado na linha {letra}.")

            if jogador_atual == 1:
                radar_jogador1 = False
            else:
                radar_jogador2 = False

            jogador_atual = trocar_jogador(jogador_atual)


def usar_radar(matriz, linha):
    for coluna in range(5):
        if matriz[linha][coluna] == '🚤':
            return True

    return False


def converter_linha(letra):
    letras = ['A', 'B', 'C', 'D', 'E']

    if letra in letras:
        return letras.index(letra)

    return -1


iniciar_jogo()