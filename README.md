
![Capa Projeto Final](https://github.com/user-attachments/assets/a9c55149-33c3-40d2-8cfa-d6ef32747c7f)


## Sobre o projeto
Este projeto foi desenvolvido totalmente em **Python** e aplica conceitos fundamentais de estruturas de dados (listas, pilhas, filas, árvores etc.) em funcionalidades como ranking de jogadores, busca por partidas e gerenciamento de dados em tempo real.

## Estrutura de pastas
```

EstruturadedadosProjeto/
├── dados/
│   └── jogadores.pkl              # Arquivo com os dados salvos dos jogadores (serializados com pickle)
│
├── plataforma_jogos/
│   ├── __init__.py                # Torna o diretório um pacote Python
│   ├── main.py                    # Arquivo principal que executa o sistema (menu, lógica principal)
│   ├── busca.py                   # Funções auxiliares de busca por jogadores e partidas
│   ├── jogador.py                 # Classe Jogador (nome, id, pontos, vitórias)
│   ├── matchmaking.py             # Função de matchmaking automático (baseada em critérios de pontuação/vitórias)
│   ├── partida.py                 # Classe Partida (jogadores, modo, ping, status, vencedor)
│   ├── ranking.py                 # Classe Ranking (adiciona, busca, atualiza e salva jogadores)
│   └── utils.py                   # Funções utilitárias (menus, limpar tela, etc.)
│
├── .gitignore                     # Arquivos/pastas ignorados pelo Git
├── LICENSE                        # Licença do projeto
└── README.md                      # Arquivo de documentação do projeto (este arquivo)


````

## Tecnologias utilizadas
- Linguagem principal: **Python**
- Estruturas de dados: listas, filas, pilhas, árvores
- Controle de versão: Git + GitHub

## Funcionalidades
- **Ranking (leaderboard):** ordena jogadores por desempenho  
- **Matchmaking:** emparelha jogadores com habilidades semelhantes  
- **Busca eficiente:** localiza rapidamente partidas ou jogadores  
- **Atualização de dados em tempo real:** mantém o sistema sincronizado dinamicamente  

## Como usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/Tutualha/EstruturadedadosProjeto.git
   ```

2. Entre na pasta:

   ```bash
   cd EstruturadedadosProjeto
   ```
3. Execute com Python (ajuste conforme o arquivo principal):

   ```bash
   python main.py
   ```

## Contribuidores

* **Heitor Sato Callejon Nóbrega** – RGM 38807742
* **Arthur Borges Miranda** – RGM 40900509
* **Pedro Henrick Lopes Oliveira** – RGM 40319946
* **Samuel Azevedo da Silva** – RGM 40025152

## Licença

Este projeto está licenciado sob a Licença **MIT**. Confira o arquivo `LICENSE` para mais detalhes.

---

Feito com a ajuda de IA para estruturar o conteúdo de forma clara e colaborativa, porem boa parte do projeto foi feito á mão 🤠.


