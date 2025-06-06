import sys
import os
# Adiciona o diretório da plataforma de jogos ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../plataforma_jogos')))


from plataforma_jogos.jogador import Jogador
from plataforma_jogos.ranking import Ranking


def testar_ranking():
    print("🔍 Testando Ranking...")
    r = Ranking()
    j1 = Jogador("PlantGamer22", 3410230, 1500, 9)
    j2 = Jogador("TrollKiller", 3410250, 1800, 2)

    r.adicionar_jogador(j1)
    r.adicionar_jogador(j2)

    r.atualizar_pontuacao("PlantGamer22", 2000)
    assert j1.pontuacao == 2000

    ranking_ordenado = sorted(r.jogadores, key=lambda j: j.pontuacao, reverse=True)
    assert ranking_ordenado[0].nome == "PlantGamer22"
    print("✅ Ranking funcionando")

if __name__ == "__main__":
    testar_ranking()
