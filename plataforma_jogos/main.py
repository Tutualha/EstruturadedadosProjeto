from matchmaking import matchmaking
from jogador import Jogador
from ranking import Ranking
from partida import Partidas
from utils import menu0_jogo, limpar_tela
import uuid
# imports:
""""uuid é usado para gerar IDs únicos para jogadores e partidas
    ultils é onde colocamos o print do menu e a função de limpar a tela
    partida é a classe que representa uma partida de jogo
    ranking é a classe que gerencia os jogadores e suas pontuações
    jogador é a classe que representa um jogador no jogo
    matchmaking é a função que busca jogadores compatíveis para partidas"""

#def onde o usuario cadastra os jogadores, com base na classe Jogador e armazenamento na classe Ranking que contem uma lista
def cadastrar_jogador(ranking):
    nome = input("Nome do jogador: ")
    pontos = int(input("Pontuação inicial: "))
    jogador_id = str(uuid.uuid4())
    jogador = Jogador(nome, jogador_id, pontos, vitorias=0)
    ranking.adicionar_jogador(jogador)

# funçao para atualizar a pontuação de um jogador, com base na classe do Ranking
def atualizar_pontuacao(ranking):
    nome = input("Nome do jogador a atualizar: ")
    nova_pontos = int(input("Nova pontuação: "))
    ranking.atualizar_pntuação(nome, nova_pontos)


def mostrar_top_jogadores(ranking):
    n = int(input("Quantos jogadores deseja ver no topo? "))
    ranking.mostrar_top(n)
    input("\nPressione Enter para continuar...")


def criar_partida_manual(ranking, partidas):
    modo = input("Modo de jogo: ")
    mapa = input("Mapa: ")
    ping = int(input("Ping médio: "))
    id_partida = str(uuid.uuid4())
    partida = Partidas(modo, mapa, ping, id_partida)

    for _ in range(2):
        nome = input("Nome do jogador: ")
        jogador = ranking.buscar_jogador(nome)
        if jogador:
            partida.adicionar_jogador(jogador)
        else:
            print("Jogador não encontrado!")

    partidas.append(partida)
    print("✅ Partida criada.")
    input("Pressione Enter para continuar...")


def exibir_partidas(partidas):
    print("🎮 Partidas criadas:")
    for i, p in enumerate(partidas, start=1):
        print(f"\nPartida {i}:")
        p.exibir_info()
    input("Pressione Enter para continuar...")


def matchmaking_automatico(ranking, partidas):
    print("🔍 Buscando partidas compatíveis...")
    partidas_criadas = matchmaking(ranking.jogadores)
    for j1, j2 in partidas_criadas:
        modo = "Automático"
        mapa = "Aleatório"
        ping = 21
        id_partida = str(uuid.uuid4())
        partida = Partidas(modo, mapa, ping, id_partida)
        partida.adicionar_jogador(j1)
        partida.adicionar_jogador(j2)
        partidas.append(partida)
        print(f"✅ Partida criada: {j1.nome} vs {j2.nome}")
    input("\nPressione Enter para continuar...")


def main():
    ranking = Ranking()
    ranking.mostrar_top()
    partidas = []

    while True:
        limpar_tela()
        opcao = menu0_jogo()

        if opcao == "1":
            cadastrar_jogador(ranking)
        elif opcao == "2":
            atualizar_pontuacao(ranking)
        elif opcao == "3":
            mostrar_top_jogadores(ranking)
        elif opcao == "4":
            criar_partida_manual(ranking, partidas)
        elif opcao == "5":
            exibir_partidas(partidas)
        elif opcao == "6":
            matchmaking_automatico(ranking, partidas)
        elif opcao == "7":
            print("🎯 Finalizar uma partida")
            for i, p in enumerate(partidas, start=1):
                print(f"{i}. Partida ID: {p.id_partida} - Jogadores: {[j.nome for j in p.jogadores]} - Status: {p.status}")

            index = int(input("Escolha o número da partida para finalizar: ")) - 1
            if 0 <= index < len(partidas):
                partida = partidas[index]
                if partida.status == "andamento":
                    print("Escolha o vencedor:")
                    for i, j in enumerate(partida.jogadores, start=1):
                        print(f"{i}. {j.nome}")
                    vencedor_index = int(input("Número do vencedor: ")) - 1
                    vencedor = partida.jogadores[vencedor_index]
                    partida.finalizar_partida(vencedor)
                    vencedor.vitorias += 1  # atualiza vitórias
                    vencedor.pontos += 10
                else:
                    print("⚠️ Essa partida já foi finalizada.")
            else:
                print("Número inválido.")
            input("Pressione Enter para continuar...")

        elif opcao == "0":
            ranking.salvar_dados()
            print("📁 Dados salvos. Encerrando...")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para tentar novamente...")
        


if __name__ == "__main__":
    main()
# plataforma_jogos/main.py