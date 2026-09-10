def tabuleiro1(n_linhas, n_colunas):
    matriz = [] 
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int(input('Digite 💧 para espaços vazios, e 🚤 para navios: '))
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

jogador1 = tabuleiro1(5,5) 
tabu = exibir_tabuleiro(jogador1)   