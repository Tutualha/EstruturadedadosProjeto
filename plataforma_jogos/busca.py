def buscar_jogadores(nome, lista_jogadores):
    print(f"\n🔍 Buscando jogador com nome contendo: '{nome}'")
    encontrados = []
    
    for jogador in lista_jogadores:
        if nome.lower() in jogador.nome.lower():
            encontrados.append(jogador)

    if encontrados:
        for j in encontrados:
            print(f"✅ Jogador encontrado: {j.nome} (ID: {j.id}) (Pontuação: {j.pontuacao})")
    else:
        print("❌ Nenhum jogador encontrado com esse nome.")
        
        
    def buscar_partidas (modo, lista_partidas):
        print(f"\n🔍 Buscando partidas no modo: '{modo}'")
        filtradas = []
        
        for partida in lista_partidas:
            if partida.modo.lower() == modo.lower():
                filtradas.append(partida)

        if filtradas:
            for p in filtradas:
                print(f"✅ Partida encontrada: {p.id} (Modo: {p.modo}) (Jogadores: {[j.nome for j in p.jogadores]}) Mapa: {p.mapa} - Ping: {p.ping}ms")
        else:
            print("❌ Nenhuma partida encontrada nesse modo.")