from jogador import Jogador

class Ranking:
    def __init__(self):
        self.jogadores = []  # lista de objetos Jogador

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def atualizar_pntuação(self, nome, nova_pontuaçao):
        for j in self.jogadores:
            if j.nome.lower() == nome.lower():
                j.pontos = nova_pontuaçao
                print(f"Pontuação de {j.nome} atualizada para {nova_pontuaçao}.")
                return
        print("Jogador não encontrado no ranking.")

    def mostrar_top(self, n=10):
        top = sorted(self.jogadores, key=lambda j: j.pontos, reverse=True)[:n]
        print(f"Top {n} jogadores:")
        for i, j in enumerate(top, start=1):
            print(f"{i}. {j.nome} - {j.pontos} pts - {j.vitorias} vitórias")

    def buscar_jogador(self, nome):
        for jogador in self.jogadores:
            if nome.lower() == jogador.nome.lower():
                return jogador
        return None