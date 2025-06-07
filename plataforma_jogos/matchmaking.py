from collections import deque
from jogador import Jogador

#função que verifica a diferença de pontos e vitorias para criar uma partida
def matchmaking(jogadores):
  jogadores_fila = deque(jogadores)    #copia a lista como deque - fila
  partida = []

  # Continua enquanto houver pelo menos dois jogadores disponíveis para formar partidas
  while len(jogadores_fila) >= 2:
    jogador =  jogadores_fila.popleft()

    for indice, adversario in enumerate(jogadores_fila):
       # Verifica se a diferença de pontos e vitórias está dentro dos limites aceitáveis
      if abs(jogador.pontos - adversario.pontos) <=200 and abs(jogador.vitorias - adversario.vitorias) <= 10:     
        partida.append((jogador, adversario))

        print(f"{jogador.nome} vs {adversario.nome}")
         # Remove o adversário da fila (pois ele já foi pareado)
        jogadores_fila.remove(adversario)
        break
      
    else:
      #joga o jogador ao final da fila se n houver partida compativel 
        jogadores_fila.append(jogador)      
        print(f"Desculpe, não foi possível achar uma partida...")

      #Se o jogador voltou para o início da fila sem encontrar par, evita repetição infinita
        if jogadores_fila[0] == jogador:    
          break

  return partida
