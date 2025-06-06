import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu0_jogo():
    print('n/---Menu Principal---')
    print('1. Cadastrar jogador')
    print('2. Iniciar partida')
    print('3. Buscar jogador')
    print('4. Ver Ranking')
    print('5. Sair')
    return input('Ecolha uma opção: ')

def pausar(): 
    input('\n Pressione Enter para continuar...')
