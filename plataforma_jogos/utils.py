import os  # Usado para limpar a tela

# Limpa o terminal (tanto no Windows qunato no Linux)
def limpar_tela(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# Mostra o menu princiapal do jogo e retorna as escolhas como str
def menu0_jogo():
    print("""
🎮 MENU PRINCIPAL
1. Adicionar jogador
2. Atualizar pontuação
3. Mostrar ranking
4. Criar partida manual
5. Mostrar partidas
6. Matchmaking automático
7. Finalizar partida
0. Salvar e sair
""")
    return input('Ecolha uma opção: ')

# pausa o programa até o usuário apertar a tecla Enter
def pausar(): 
    input('\n Pressione Enter para continuar...')
