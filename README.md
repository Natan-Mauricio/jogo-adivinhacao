# 🎮 Jogo da Adivinhação

Projeto simples desenvolvido em Python utilizando conceitos de Programação Orientada a Objetos (POO) e princípios SOLID.

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

- **`O projeto segue uma arquitetura orientada a objetos, desenvolvido aplicando boas práticas de programação, como`**:
  - `Abstração`: Classe base `Jogo` define métodos genéricos como `iniciar()` e `jogar()`.
  - `Encapsulamento`: Uso de atributos privados como `__numero_secreto`.
  - `Herança`: Classe `JogoAdivinhacao` herda da classe `Jogo`.
  - `Polimorfismo`: Métodos `iniciar()` e `jogar()` são implementados de formas diferentes.
  - `Princípios SOLID`: Aplicação de princípios como SRP, OCP, LSP, ISP e DIP.
- **`E com as seguintes classes`**:

## Classes Principais

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

## 💡 Exemplo de Jogo

'''
============================================================
             =====< JOGO DA ADIVINHAÇÃO >=====              
============================================================
                        Como jogar:                         
       Tente adivinhar o número secreto entre 1 e 100       
============================================================
                        Dificuldade:                        
1. Fácil -> 15 tentativas
2. Médio -> 10 tentativas
3. Difícil -> 5 tentativas
Escolha (1 a 3): 3
============================================================
                          Jogador:                          
Digite seu nome: Natan
============================================================
                        Advinhação:                         
Tentativa 1: 50
O número secreto é menor.
Tentativa 2: 25
O número secreto é maior.
Tentativa 3: 35
O número secreto é maior.
Tentativa 4: 42
O número secreto é maior.
Tentativa 5: 46
============================================================
Parabéns! Você acertou!
Tentativas usadas: 5
============================================================
                          Ranking:                          
1º Natan - 270
============================================================
Continuar? (s/n): s
============================================================
             =====< JOGO DA ADIVINHAÇÃO >=====              
============================================================
                        Como jogar:                         
       Tente adivinhar o número secreto entre 1 e 100       
============================================================
                        Dificuldade:                        
1. Fácil -> 15 tentativas
2. Médio -> 10 tentativas
3. Difícil -> 5 tentativas
Escolha (1 a 3): 1
============================================================
                          Jogador:                          
Digite seu nome: Natan
============================================================
                        Advinhação:                         
Tentativa 1: 50
O número secreto é maior.
Tentativa 2: 75
O número secreto é maior.
Tentativa 3: 85
O número secreto é maior.
Tentativa 4: 95
O número secreto é menor.
Tentativa 5: 90
O número secreto é maior.
Tentativa 6: 92
============================================================
Parabéns! Você acertou!
Tentativas usadas: 6
============================================================
                          Ranking:                          
1º Natan - 350
============================================================
Continuar? (s/n): s
============================================================
             =====< JOGO DA ADIVINHAÇÃO >=====              
============================================================
                        Como jogar:                         
       Tente adivinhar o número secreto entre 1 e 100       
============================================================
                        Dificuldade:                        
1. Fácil -> 15 tentativas
2. Médio -> 10 tentativas
3. Difícil -> 5 tentativas
Escolha (1 a 3): 2
============================================================
                          Jogador:                          
Digite seu nome: Jorge
============================================================
                        Advinhação:                         
Tentativa 1: 50
O número secreto é menor.
Tentativa 2: 25
O número secreto é menor.
Tentativa 3: 15
O número secreto é menor.
Tentativa 4: 10
O número secreto é maior.
Tentativa 5: 13
============================================================
Parabéns! Você acertou!
Tentativas usadas: 5
============================================================
                          Ranking:                          
1º Natan - 350
2º Jorge - 180
============================================================
Continuar? (s/n): n
'''

## 🚀 Como Executar

## Pré-requisitos
- Python 3.6 ou superior

## Instalação
- **`1. Clone o repositório`**:
  - ```bash
  - git clone https://github.com/seu-usuario/jogo-adivinhacao.git
- **`2. Execute`**:
  - cd jogo-adivinhacao

## 🎯 Melhorias Futuras

- **`Salvar ranking em arquivo para persistência`**
- **`Adicionar diferentes modos de jogo`**
- **`Implementar interface gráfica (GUI)`**

## 👨‍💻 Autor

- **`Natan Maurício da Silva`**  
