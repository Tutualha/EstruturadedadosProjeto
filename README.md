
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

## Principais Componentes 🧩
Aqui está o que cada arquivo, classe e objeto representa no projeto

| Módulo           | Descrição                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| `main.py`        | Ponto de entrada do sistema. Menu principal e chamadas de função.                                        |
| `jogador.py`     | Define a estrutura e atributos dos jogadores.                                                            |
| `partida.py`     | Representa uma partida entre jogadores, com suporte para adicionar jogadores, finalizar e exibir status. |
| `ranking.py`     | Gera e gerencia o ranking dos jogadores, incluindo persistência via `pickle`.                            |
| `matchmaking.py` | Implementa um sistema de matchmaking automático baseado em critérios de pontuação e vitórias.            |                                    |
| `utils.py`       | Contém funções auxiliares para menus, interação com o usuário e limpeza de tela.                         |



## Tecnologias utilizadas
- Linguagem principal: **Python**
- Estruturas de dados utilizadas: 
  - **Listas** para ranking e armazenamento de jogadores
  - **Filas (`deque`)** no sistema de matchmaking
  - **Pilhas e árvores** (simuladas/conceituais conforme solicitado pelo projeto)
- Utilizamos libs como a uuid para criar ids para os jogadores e as partidas, deque() e pickle.

   deque vem do módulo collections do Python e significa fila de duas pontas.
   
   O módulo pickle do Python é usado para salvar objetos...
- Controle de versão: Git + GitHub

## Funcionalidades
- **Ranking (leaderboard):** ordena jogadores por desempenho  
- **Matchmaking:** emparelha jogadores com habilidades semelhantes  
- **Busca eficiente:** localiza rapidamente partidas ou jogadores  
- **Atualização de dados em tempo real:** mantém o sistema sincronizado dinamicamente 

## 💾 Salvamento de Dados
Os dados dos jogadores são salvos em dados/jogadores.pkl automaticamente ao sair do sistema (opção 0 do menu).

O formato usado é pickle, ideal para serializar objetos Python de forma simples e eficiente.

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


