from collections import deque
from jogador import Jogador

def Matchmaking(jogadores):
  jogadores_fila = deque(jogadores)    #copia a lista como deque - fila
  partida = []

  while len(jogadores_fila) >= 2:
    jogador =  jogadores_fila.popleft()

    for indice, adversario in enumerate(jogadores_fila):
      if abs(jogador.pontos - adversario.pontos) <=200 and abs(jogador.vitorias - adversario.vitorias) <= 10:     #verifica a diferença de pontos e vitorias para criar uma partida
        partida.append((jogador, adversario))

        print(f"{jogador.nome} vs {adversario.nome}")
        jogadores_fila.remove(adversario)
        break
      
    else:
        jogadores_fila.append(jogador)  #joga o jogador ao final da fila se n houver partida compativel 
        print(f"Desculpe, não foi possível achar uma partida...")

        if jogadores_fila[0] == jogador:
          break

  return partida
