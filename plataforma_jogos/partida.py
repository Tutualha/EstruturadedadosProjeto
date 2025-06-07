from jogador import Jogador

# Inicia a partida de acordo com mapa, ping e modo
class Partidas:
    def __init__(self, modo, mapa, ping, id_partida):
        self.id_partida = id_partida
        self.mapa = mapa
        self.ping = ping
        self.modo = modo
        self.jogadores = [] # Lista de jogadores
        self.status = "andamento" 
        self.vencedor = {}
        
    # A partida inicia quando encontrar os 2 players   
    def adicionar_jogador(self, jogador):
        if len(self.jogadores) < 2:
            self.jogadores.append(jogador)
            print(f"Jogador {jogador.nome} adicionado à partida {self.id_partida}.")
        # Retorna caso se a partida tiver mais que 2 players
        else:
            print(f"Partida {self.id_partida} já está cheia. Não é possível adicionar mais jogadores.")
            
    # Finaliza a partida e informa o vencedor       
    def finalizar_partida(self, vencedor):
        self.vencedor = vencedor
        self.status = "finalizada"
        print(f"Partida {self.id_partida} finalizada. Vencedor: {vencedor.nome}.")

     # Mostra as informações da partida como: modo, mapa, ping e vencedor(se caso haver vencedor)
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
    
