import os  # Usado para limpar a tela

# Limpa o terminal (tanto no Windows qunato no Linux)
def limpar_tela(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# Mostra o menu princiapal do jogo e retorna as escolhas como str
def menu_jogo():
    print('n/---Menu Principal---')
    print('1. Criar jogador')
    print('2. Atualizar pontuação')
    print('3. Classificação ')
    print('4. Modo de jogo')
    print('5. Iniciar partida')
    print("6. Matchmaking automático")
    print('0. Salvar e sair.')
    return input('Ecolha uma opção: ')

# pausa o programa até o usuário apertar a tecla Enter
def pausar(): 
    input('\n Pressione Enter para continuar...')
