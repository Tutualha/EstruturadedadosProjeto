# classe Jogador
class Jogador:
    # iniciando atributos da classe Jogador
    def __init__(self, nome, id, pontos= 0, vitorias= 0): # init é o construtor da classe
        self.nome = nome # nome do jogador
        self.id = id # id do jogador
        self.pontos = pontos # pontos do jogador
        self.vitorias = vitorias # vitorias do jogador
    # metodo para representar o objeto Jogador e facilitando sua impressao
    
    def __str__(self): # método especial que define como o objeto é representado como string
        return f"Jogador: {self.nome}, Pontos: {self.pontos}, Vitórias: {self.vitorias}" # método que retorna uma string formatada com os atributos do jogador
    