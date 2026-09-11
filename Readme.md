# 🚢 Jogo de Batalha Naval

Projeto desenvolvido em Python para a disciplina de **Computational Thinking using Python**, com o objetivo de aplicar os principais conceitos estudados durante as aulas por meio da criação de um jogo de tabuleiro.

O projeto é baseado no jogo Batalha Naval e possui uma mecânica adicional de **Radar**, que adiciona uma nova possibilidade estratégica durante a partida.

---

## 🎯 Objetivo do Jogo

O jogo é disputado entre **dois jogadores**.

Cada jogador possui um tabuleiro **5x5** e deve posicionar **3 navios** antes do início da partida.

Depois do posicionamento, os jogadores alternam seus turnos tentando encontrar e destruir os navios adversários.

O primeiro jogador que conseguir atingir os três navios do oponente vence a partida.

---

## 🎮 Como funciona

O tabuleiro possui:

- Linhas identificadas pelas letras **A, B, C, D e E**;
- Colunas identificadas pelos números **0, 1, 2, 3 e 4**;
- 3 navios para cada jogador;
- Cada navio ocupa uma única posição do tabuleiro.

Exemplo de coordenada:

`B3`

Nesse caso:

- `B` representa a linha;
- `3` representa a coluna.

Durante seu turno, o jogador pode escolher entre:

1. **Atacar uma posição**
2. **Utilizar o radar**

Após uma ação válida, o turno passa para o outro jogador.

---

## 🗺️ Símbolos do Tabuleiro

| Símbolo | Significado |
|---|---|
| 💧 | Água |
| 🚤 | Navio |
| 💥 | Navio atingido |
| ❌ | Tiro na água |

Durante a fase de ataques, os navios que ainda não foram atingidos ficam escondidos do adversário e aparecem como água.

---

## 🚤 Posicionamento dos Navios

Antes da partida, cada jogador posiciona seus **3 navios**.

O jogador informa uma linha entre **A e E** e uma coluna entre **0 e 4**.

O programa verifica se:

- A coordenada está dentro dos limites do tabuleiro;
- Já existe um navio naquela posição.

Caso a posição seja inválida ou já esteja ocupada, o jogador deve escolher outra coordenada.

---

## 💥 Sistema de Ataques

A função `verificar_jogada()` é responsável por analisar cada ataque realizado durante a partida.

```python
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
```

### Validação de limites

A condição:

```python
if not (0 <= linha < 5 and 0 <= coluna < 5):
```

verifica se a posição informada existe dentro da matriz 5x5. Dessa forma, o programa evita tentar acessar uma posição inexistente do tabuleiro.

As letras **A até E** informadas pelo jogador são convertidas internamente para posições numéricas de **0 até 4**.

### Leitura da posição

```python
posicao = matriz[linha][coluna]
```

O conteúdo da posição escolhida é armazenado na variável `posicao` para que o programa possa identificar o resultado do ataque.

### Acerto em um navio

Se a posição possuir um navio (`🚤`), ela é alterada para uma explosão (`💥`), registrando que aquele navio foi atingido.

### Tiro na água

Se a posição possuir água (`💧`), ela é alterada para `❌`, registrando que aquela posição já recebeu um ataque.

### Jogada repetida

Se a posição já possuir `💥` ou `❌`, significa que ela já foi atacada anteriormente.

Nesse caso, o programa informa o jogador e permite que ele tente novamente, sem perder o turno.

---

## 📡 Sistema de Radar

Além do ataque tradicional, o jogo possui uma mecânica especial de **Radar**.

Cada jogador pode utilizar o radar **uma única vez durante toda a partida**.

Ao utilizar o radar:

1. O jogador escolhe uma linha entre **A e E**;
2. O sistema verifica essa linha do tabuleiro adversário;
3. O radar informa se existe pelo menos um navio ainda não atingido naquela linha;
4. A coluna exata do navio não é revelada;
5. O uso do radar consome o turno do jogador.

Exemplo:

```text
Digite a linha que deseja escanear (A a E): C
📡 Radar detectou um navio na linha C!
```

O radar adiciona uma decisão estratégica ao jogo: o jogador pode gastar seu turno para obter uma pista sobre a localização dos navios adversários.

---

## 🏆 Condição de Vitória

A função `verificar_vitoria()` percorre o tabuleiro adversário procurando navios que ainda não foram atingidos.

```python
def verificar_vitoria(matriz):
    for linha in matriz:
        for posicao in linha:
            if posicao == '🚤':
                return False

    return True
```

Enquanto existir pelo menos um `🚤`, a partida continua.

Quando nenhum navio permanecer no tabuleiro, significa que todos foram atingidos e o jogador responsável pelo último ataque vence a partida.

---

## 🔄 Sistema de Turnos

Os jogadores alternam seus turnos durante a partida.

A função `trocar_jogador()` é responsável por realizar essa troca:

```python
def trocar_jogador(jogador_atual):
    if jogador_atual == 1:
        return 2
    else:
        return 1
```

Após um ataque válido ou o uso do radar, o turno passa para o adversário.

Jogadas inválidas ou ataques em posições que já foram utilizadas não consomem o turno.

---

## 🧩 Principais Funções

### `criar_tabuleiro()`

Cria a matriz que representa o tabuleiro e preenche inicialmente todas as posições com água.

### `posicionar_navios()`

Permite que o jogador escolha as posições dos seus três navios e valida as coordenadas informadas.

### `exibir_tabuleiro()`

Exibe o tabuleiro completo do jogador, incluindo seus próprios navios.

### `exibir_tabuleiro_ataque()`

Exibe o tabuleiro durante a fase de ataque, escondendo os navios adversários que ainda não foram atingidos.

### `verificar_jogada()`

Verifica o resultado de um ataque e atualiza a posição correspondente no tabuleiro.

### `verificar_vitoria()`

Verifica se ainda existem navios não atingidos no tabuleiro adversário.

### `trocar_jogador()`

Alterna o turno entre o Jogador 1 e o Jogador 2.

### `usar_radar()`

Percorre a linha escolhida e informa se existe algum navio ainda não atingido nela.

### `converter_linha()`

Converte as letras das linhas para índices que podem ser utilizados pela matriz.

Exemplo:

```text
A → 0
B → 1
C → 2
D → 3
E → 4
```

### `iniciar_jogo()`

Controla o fluxo principal da partida, incluindo a criação dos tabuleiros, posicionamento dos navios, ataques, radar, troca de turnos e condição de vitória.

---

## 🧠 Conceitos de Python Utilizados

Durante o desenvolvimento foram utilizados conceitos estudados na disciplina, como:

- Variáveis;
- Strings;
- Listas;
- Listas de listas (matriz);
- Estruturas condicionais `if`, `elif` e `else`;
- Laços de repetição `for` e `while`;
- Funções;
- Parâmetros;
- Retorno de valores com `return`;
- Tratamento de erros com `try` e `except`;
- Manipulação e validação de dados.

O estado principal da partida é mantido dentro das funções, evitando a utilização de variáveis globais para controlar o jogo.

---

## ▶️ Como Executar

É necessário possuir o **Python** instalado no computador.

Clone ou baixe este repositório e abra o terminal na pasta do projeto.

Execute:

```bash
python main.py
```

Depois, basta seguir as instruções exibidas no terminal.

---

## 📋 Regras Resumidas

1. Cada jogador posiciona 3 navios.
2. Os jogadores alternam seus turnos.
3. Em cada turno é possível atacar ou utilizar o radar.
4. Cada jogador possui apenas um uso do radar.
5. O radar informa apenas se existe um navio não atingido na linha escolhida.
6. Ataques repetidos ou inválidos não consomem o turno.
7. O radar consome o turno.
8. O primeiro jogador que destruir os 3 navios adversários vence.

---

## 👥 Integrantes

- Erick Menezes — RM570325
- Luiz Henrique Albarello — RM572727
- Matheus Yudi — RM571245
- Matheus Rodrigues — RM570469

---

## 📚 Disciplina

**Computational Thinking using Python**

