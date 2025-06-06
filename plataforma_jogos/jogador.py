# classe Jogador
class Jogador:
    # iniciando atributos da classe Jogador
    def __init__(self, nome, id, pontos= 0, vitorias= 0):
        self.nome = nome
        self.id = id
        self.pontos = pontos
        self.vitorias = vitorias
    # metodo para representar o objeto Jogador e facilitando sua impressao
    def __str__(self):
        return f"Jogador: {self.nome}, Pontos: {self.pontos}, Vitórias: {self.vitorias}"
    