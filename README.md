# 🎮 Jogo da Adivinhação

Um jogo de adivinhação interativo desenvolvido em Python, onde o jogador tenta descobrir um número secreto com um sistema de pontuação baseado em desempenho e ranking integrado.

## 📋 Descrição

O Jogo da Adivinhação é uma implementação orientada a objetos que desafia os jogadores a adivinhar um número secreto entre 1 e 100. O jogo oferece diferentes níveis de dificuldade, um sistema de pontuação progressiva e um ranking para acompanhar os melhores desempenhos.

## ✨ Funcionalidades

- 🎯 **Três níveis de dificuldade**:
  - Fácil: 15 tentativas
  - Médio: 10 tentativas
  - Difícil: 5 tentativas

- 📊 **Sistema de pontuação dinâmico**: Quanto menos tentativas, maior a pontuação
- 🏆 **Ranking persistente**: Acompanha todos os jogadores e suas pontuações
- 🔄 **Múltiplas partidas**: Possibilidade de jogar várias vezes consecutivas
- 🎨 **Interface amigável**: Feedback claro e visual organizado

## 🏗️ Estrutura do Projeto

O projeto segue uma arquitetura orientada a objetos com as seguintes classes:

### Classes Principais

- **`Jogo`** (ABC): Classe abstrata que define o contrato para todos os jogos
  - `iniciar()`: Prepara o jogo
  - `jogar()`: Executa a lógica principal
  - `pontuar()`: Calcula a pontuação
  - `ranking()`: Exibe o ranking
  - `escolher_dificuldade()`: Define o nível de dificuldade

- **`Jogador`**: Gerencia os dados do jogador
  - Encapsulamento dos atributos `nome` e `pontuacao`
  - Getters e setters para acesso controlado

- **`Ranking`**: Gerencia o sistema de classificação
  - `adicionar()`: Insere ou atualiza jogador no ranking
  - `exibir()`: Mostra ranking ordenado por pontuação

- **`JogoAdivinhacao`**: Implementação concreta do jogo
  - Lógica completa do jogo de adivinhação
  - Sistema de pontuação baseado em tentativas e dificuldade

## 📊 Sistema de Pontuação
- **`A pontuação é calculada pela fórmula`**:
  - Pontos = PontosBase(tentativa) × Dificuldade
- **`Onde`**:
  - PontosBase: 130, 120, 110, 100, 90, 80, 80, 70, 60, 50, 40, 30, 20, 10, 5 (respectivamente da 1ª à 15ª tentativa)
  - Dificuldade: 1 (Fácil), 2 (Médio), 3 (Difícil)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/jogo-adivinhacao.git
cd jogo-adivinhacao

