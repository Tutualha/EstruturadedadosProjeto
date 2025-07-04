from jogador import Jogador
import pickle
class Ranking:
    def __init__(self):
        self.jogadores = []  # lista de objetos Jogador
        self.jogadores = self.carregar_dados()

    # Adiciona um jogador no Ranking
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    # Atualiza as pontuações do jogador
    def atualizar_pntuação(self, nome, nova_pontuaçao):
        for j in self.jogadores:
            if j.nome.lower() == nome.lower():
                j.pontos = nova_pontuaçao
                print(f"Pontuação de {j.nome} atualizada para {nova_pontuaçao}.")
                return
        print("Jogador não encontrado no ranking.")

    # Mostra o top N jogadores com as maiores pontuações 
    def mostrar_top(self, n=10):
        top = sorted(self.jogadores, key=lambda j: j.pontos, reverse=True)[:n]
        print(f"Top {n} jogadores:")
        for i, j in enumerate(top, start=1):
            print(f"{i}. {j.nome} - {j.pontos} pts - {j.vitorias} vitórias")

    # Busca um jogador expecífico
    def buscar_jogador(self, nome):
        for jogador in self.jogadores:
            if nome.lower() == jogador.nome.lower():
                return jogador
        return None
    
    def salvar_dados(self):
        with open("jogadores.pkl", "wb") as f:
            pickle.dump(self.jogadores, f)

    def carregar_dados(self):
        try:
            with open("jogadores.pkl", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []