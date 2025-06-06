import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from plataforma_jogos.jogador import Jogador
from plataforma_jogos.partida import Partidas


def testar_partida():
    print("🔍 Testando Partida...")
    j1 = Jogador("PlantGamer22", 3410230, 1500, 9)
    j2 = Jogador("TrollKiller", 3410250, 1800, 2)

    p = Partidas("Deathmatch", "Dust2", 50)
    p.adicionar_jogador(j1)
    p.adicionar_jogador(j2)

    assert len(p.jogadores) == 2
    p.finalizar_partida({"PlantGamer22": 8, "TrollKiller": 5})
    assert p.status == "finalizada"
    assert p.resultado["PlantGamer22"] == 8
    print("✅ Partida funcionando")

if __name__ == "__main__":
    testar_partida()