class Jogador:
    def __init__(self, nome, id, pontos, vitorias):
        self.nome = ""
        self.id = 0
        self.pontos = 0
        self.vitorias = 0
    
    def __str__(self):
        return f"Jogador: {self.nome}, Pontos: {self.pontos}, Vitórias: {self.vitorias}"
    