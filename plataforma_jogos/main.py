from jogador import Jogador
from ranking import Ranking
from partida import Partida
from utils import menu_principal, limpar_tela

def main():
    ranking = Ranking()
    ranking.carregar_dados()

    partidas = []  # Lista de Partida (pode ser salva em JSON depois)

    while True:
        limpar_tela()
        opcao = menu_principal()

        if opcao == "1":
            nome = input("Nome do jogador: ")
            pontuacao = int(input("Pontuação inicial: "))
            jogador = Jogador(nome, pontuacao)
            ranking.adicionar_jogador(jogador)

        elif opcao == "2":
            nome = input("Nome do jogador a atualizar: ")
            nova_pontuacao = int(input("Nova pontuação: "))
            ranking.atualizar_pontuacao(nome, nova_pontuacao)

        elif opcao == "3":
            n = int(input("Quantos jogadores deseja ver no topo? "))
            ranking.mostrar_top(n)
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            modo = input("Modo de jogo: ")
            mapa = input("Mapa: ")
            ping = int(input("Ping médio: "))
            partida = Partida(modo, mapa, ping)

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

        elif opcao == "0":
            ranking.salvar_dados()
            print("📁 Dados salvos. Encerrando...")
            break

        else:
            print("Opção inválida!")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()
