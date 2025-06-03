class Ranking:
    def __init__(self):
        self.jogadores = [] # lista de objetos Jogador
        
        
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        
    def atualizar_pntuação(self, nome, nova_pontuaçao):
        for j in  self.jogadores:
            if j.nome.lower() == nome.lower():
                j.pontuacao = nova_pontuaçao
                print (f"Pontuação de {j.nome} atualizada para {nova_pontuaçao}.")
                return
        print(f"Jogador não encontrado no ranking.")
        
    def mostrar_top(self, n=10):
        print(f"Top {n} jogadores:")
        ordenados = sorted(self.jogadores, key=lambda j: j.pontuacao, reverse=True)
        for i, jogador in enumerate(ordenados[:n], start=1):
            print(f"{i}. {jogador.nome} - {jogador.pontuacao} pontos")