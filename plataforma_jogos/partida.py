from jogador import Jogador

class Partidas:
    def __init__(self, modo, mapa, ping, id_partida):
        self.id_partida = id_partida
        self.mapa = mapa
        self.ping = ping
        self.modo = modo
        self.jogadores = []
        self.status = "andamento" 
        self.vencedor = {}
        
        
    def adicionar_jogador(self, jogador):
        if len(self.jogadores) < 2:
            self.jogadores.append(jogador)
            print(f"Jogador {jogador.nome} adicionado à partida {self.id_partida}.")
        else:
            print(f"Partida {self.id_partida} já está cheia. Não é possível adicionar mais jogadores.")
            
            
    def finalizar_partida(self, vencedor):
        self.vencedor = vencedor
        self.status = "finalizada"
        print(f"Partida {self.id_partida} finalizada. Vencedor: {vencedor.nome}.")
        
    def exibir_info(self):
        print(f"Partida ID: {self.id_partida}")
        print(f"Modo: {self.modo}")
        print(f"Mapa: {self.mapa}")
        print(f"Ping: {self.ping} ms")
        print(f"Status: {self.status}")
        if self.vencedor:
            print(f"Vencedor: {self.vencedor.nome}")
        else:
            print("Ainda não há vencedor.")
        
        print("Jogadores na partida:")
        for jogador in self.jogadores:
            print(f"- {jogador.nome} (ID: {jogador.id})")
    
