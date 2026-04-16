import random
from abc import ABC, abstractmethod

class Jogo(ABC):

  @abstractmethod
  def iniciar(self):
    pass

  @abstractmethod
  def jogar(self):
    pass

  @abstractmethod
  def pontuar(self):
    pass

  def ranking(self):
    pass

  def escolher_dificuldade(self):
    pass

# Classe jogador separada (armazena nome e pontuação)
class Jogador():

  def __init__(self, nome, pontuacao):
    self.__nome = nome
    self.__pontuacao = pontuacao

  def get_nome(self):
    return self.__nome

  def get_pontuacao(self):
    return self.__pontuacao

  def set_nome(self, nome):
    self.__nome = nome

  def set_pontuacao(self, pontuacao):
    self.__pontuacao = pontuacao

# Sistema de Ranking:
class Ranking():

  def __init__(self, jogadores):
    self.__jogadores = jogadores

  def adicionar(self, nome, pontos):
    for jogador in self.__jogadores:
      if jogador["nome"] == nome:
        jogador["pontos"] += pontos
        return

    self.__jogadores.append({"nome": nome, "pontos": pontos})

# Exibe ranking ordenado:
  def exibir(self):
    jogadores_ordenados = sorted(self.__jogadores, key=lambda x: x["pontos"], reverse=True)

    print(f"{'=' * 60}")
    print(f"{'Ranking:':^60}")
    for i, jogador in enumerate(jogadores_ordenados, start=1):
      print(f"{i}º {jogador['nome']} - {jogador['pontos']}")
    print(f"{'=' * 60}")

class JogoAdivinhacao(Jogo):

  def __init__(self, jogador: Jogador, ranking: Ranking):
    self.__jogador = jogador
    self.__ranking = ranking
    self.__numero_secreto = 0 # Aleatório (1 a 100)
    self.__tentativas = 0 # De acordo com as tentativas do Jogador
    self.__limite = 0 # Depende da dificuldade
    self.__dificuldade = 0 # Definido pelo Jogador

# Função que define diculdade e limite de tentativas
  def escolher_dificuldade(self):
    print("1. Fácil -> 15 tentativas\n"
        "2. Médio -> 10 tentativas\n"
        "3. Difícil -> 5 tentativas")
    escolha = validar_entrada(int, [1, 2, 3], 'Escolha (1 a 3): ')
    self.__dificuldade = escolha
    self.__limite = {1: 15, 2: 10, 3: 5}[self.__dificuldade]

  def iniciar(self):
    self.__tentativas = 0
    self.__numero_secreto = random.randint(1, 100)

    print(f"{'=' * 60}")
    print(f"{'=====< JOGO DA ADIVINHAÇÃO >=====':^60}")
    print(f"{'=' * 60}\n{'Como jogar:':^60}\n{'Tente adivinhar o número secreto entre 1 e 100':^60}")
    print(f"{'=' * 60}")

    print(f"{'Dificuldade:':^60}")
    self.escolher_dificuldade()
    print(f"{'=' * 60}")

    print(f"{'Jogador:':^60}")
    nome = input(("Digite seu nome: "))
    self.__jogador.set_nome(nome)
    print(f"{'=' * 60}")

# Sistema de pontuação baseado em desempenho
  def pontuar(self, acertou):
    # Acertos: Pontos
    tabela = {
    1: 130, 2: 120, 3: 110, 4: 100, 5: 90,
    6: 80, 7: 80, 8: 70, 9: 60, 10: 50,
    11: 40, 12: 30, 13: 20, 14: 10, 15: 5
    }
    if acertou:
      # Pontuação depende de tentativas e dificuldade
        pontos = tabela.get(self.__tentativas) * self.__dificuldade
    else:
        pontos = 0

    self.__jogador.set_pontuacao(pontos)

# Função que adiciona jogador no ranking e exibe
  def ranking(self):
    self.__ranking.adicionar(self.__jogador.get_nome(), self.__jogador.get_pontuacao())
    self.__ranking.exibir()

  def jogar(self):
    print(f"{'Advinhação:':^60}")
    while self.__tentativas < self.__limite:
      mensagem = f'Tentativa {self.__tentativas + 1}: '
      palpite = validar_entrada(int, range(1, 101), mensagem)
      self.__tentativas += 1

      if palpite == self.__numero_secreto:
        print(f"{'=' * 60}")
        print("Parabéns! Você acertou!")
        print("Tentativas usadas:", self.__tentativas)
        self.pontuar(acertou = True)
        self.ranking()
        return

      elif palpite < self.__numero_secreto:
        print("O número secreto é maior.")
      else:
        print("O número secreto é menor.")

    print(f"{'=' * 60}")
    print("Suas tentativas acabaram!")
    print("O número secreto era:", self.__numero_secreto)
    self.pontuar(acertou = False)
    self.ranking()

def validar_entrada(tipo, opcoes, mensagem):
  while True:
    try:
      entrada = tipo(input(mensagem))
      if entrada in opcoes:
        break
      else:
        raise ValueError
    except:
      print("Entrada Inválida. Tente Novamente...")
      continue
  return entrada

# Loop para jogar várias vezes
def executar_jogo(jogo: Jogo):
  escolha = 's'
  while escolha == 's':
    jogo.iniciar()
    jogo.jogar()
    escolha = validar_entrada(str, ['s', 'S', 'n', 'N'], 'Continuar? (s/n): ')

jogador = Jogador("Nome", 0)
ranking = Ranking([])
jogo = JogoAdivinhacao(jogador, ranking)
executar_jogo(jogo)
