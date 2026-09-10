Para o Matheus

## A Função de Verificação de Jogada

```python
def verificar_jogada(matriz, linha, coluna):
    # 1. Validação de limites
    if not (0 <= linha < 5 and 0 <= coluna < 5):
        return "Coordenada inválida! Escolha números entre 0 e 4."
    
    # 2. Leitura da posição
    posicao = matriz[linha][coluna]
    
    # 3. Tratamento de acerto
    if posicao == '🚤':
        matriz[linha][coluna] = '💥'
        return "Acertou em cheio! 💥"
    
    # 4. Tratamento de erro na água
    elif posicao == '💧':
        matriz[linha][coluna] = '❌'
        return "Água! ❌"
        
    # 5. Tratamento de jogada repetida
    elif posicao == '💥' or posicao == '❌':
        return "Você já atirou nessa posição! Tente outra."
        
    return "Posição desconhecida."

Validação de Limites (if not (0 <= linha < 5 and 0 <= coluna < 5):): Verifica se os números informados estão dentro do tamanho do tabuleiro (que vai de 0 a 4). Se o jogador digitar um número menor que 0 ou maior/igual a 5, a função barra a jogada imediatamente com uma mensagem de erro, evitando que o programa feche sozinho por tentar acessar uma posição que não existe.

Leitura da Posição (posicao = matriz[linha][coluna]): Guarda o conteúdo atual que está salvo naquela coordenada específica do tabuleiro para sabermos o que o jogador atingiu.

Acerto em Navio (if posicao == '🚤':): Se a posição escolhida continha um navio, o código altera o valor daquela célula na matriz para uma explosão (💥) e retorna a mensagem de acerto.

Tiro na Água (elif posicao == '💧':): Se a posição continha água, o código substitui o espaço por um marcador de tiro errado (❌) para registrar que aquele espaço já foi jogado.

Jogada Repetida (elif posicao == '💥' or posicao == '❌':): Verifica se o espaço escolhido já havia sido atingido antes. Caso afirmativo, impede que o jogador gaste a jogada no mesmo lugar e avisa que ele precisa escolher outra coordenada.