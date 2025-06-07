import matchmaking
from jogador import Jogador
from ranking import Ranking
from partida import Partidas
from utils import menu0_jogo, limpar_tela
import uuid

def main():
    ranking = Ranking()
    ranking.mostrar_top()

    partidas = []  # Lista de Partida (pode ser salva em JSON depois)

    while True:
        limpar_tela()
        opcao = menu0_jogo()

        if opcao == "1":
            nome = input("Nome do jogador: ")
            pontos = int(input("Pontuação inicial: "))
            jogador_id = str(uuid.uuid4())  # Gera ID único
            jogador = Jogador(nome, jogador_id, pontos, vitorias=0)
            ranking.adicionar_jogador(jogador)

        elif opcao == "2":
            nome = input("Nome do jogador a atualizar: ")
            nova_pontos = int(input("Nova pontuação: "))
            ranking.atualizar_pntuação(nome, nova_pontos)

        elif opcao == "3":
            n = int(input("Quantos jogadores deseja ver no topo? "))
            ranking.mostrar_top(n)
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            modo = input("Modo de jogo: ")
            mapa = input("Mapa: ")
            ping = int(input("Ping médio: "))
            id_partida = str(uuid.uuid4())  # Gera ID único para a partida
            partida = Partidas(modo, mapa, ping, id_partida)

            for _ in range(2):  # Simplesmente adiciona dois jogadores
                nome = input("Nome do jogador: ")
                jogador = ranking.buscar_jogador(nome)
                if jogador:
                    partida.adicionar_jogador(jogador)
                else:
                    print("Jogador não encontrado!")

            partidas.append(partida)
            print("✅ Partida criada.")
            input("Pressione Enter para continuar...")

        elif opcao == "5":
            print("🎮 Partidas criadas:")
            for i, p in enumerate(partidas, start=1):
                print(f"\nPartida {i}:")
                p.exibir_info()
            input("Pressione Enter para continuar...")
        
        elif opcao == "6":
            partidas_geradas = matchmaking(ranking.jogadores)
            for j1, j2 in partidas_geradas:
                id_partida = str(uuid.uuid4())
                nova_partida = Partidas("Matchmaking", "Mapa Padrão", 50, id_partida)
                nova_partida.adicionar_jogador(j1)
                nova_partida.adicionar_jogador(j2)
                partidas.append(nova_partida)
                print(f"✅ Partida entre {j1.nome} e {j2.nome} criada.")
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
