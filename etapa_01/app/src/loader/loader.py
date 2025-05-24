from app.src.graph.graph import Multigraph

def carregar_instancia(caminho_arquivo):
    grafo = Multigraph()
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]

    secao = None
    for linha in linhas:
        if linha.startswith(("Name", "Optimal", "#", "the data is")):
            continue

        if "ReN." in linha:
            secao = "nos_obrigatorios"
            continue
        elif "ReE." in linha:
            secao = "arestas_obrigatorias"
            continue
        elif "EDGE" in linha:
            secao = "arestas_nao_obrigatorias"
            continue
        elif "ReA." in linha:
            secao = "arcos_obrigatorios"
            continue
        elif "ARC" in linha:
            secao = "arcos_nao_obrigatorios"
            continue

        if secao:
            partes = linha.split()
            try:
                if secao == "nos_obrigatorios":
                    no = int(partes[0].replace("N", ""))
                    demanda, custo_s = map(int, partes[1:3])
                    grafo.adicionar_no_obrigatorio(no, demanda, custo_s)

                elif secao == "arestas_obrigatorias":
                    origem = int(partes[1])
                    destino = int(partes[2])
                    custo_transporte = int(partes[3])
                    demanda = int(partes[4])
                    custo_s = int(partes[5])
                    grafo.adicionar_aresta_obrigatoria(origem, destino, custo_transporte, demanda, custo_s)

                elif secao == "arcos_obrigatorios":
                    origem = int(partes[1])
                    destino = int(partes[2])
                    custo_transporte = int(partes[3])
                    demanda = int(partes[4])
                    custo_s = int(partes[5])
                    grafo.adicionar_arco_obrigatorio(origem, destino, custo_transporte, demanda, custo_s)

                elif secao == "arestas_nao_obrigatorias":
                    origem = int(partes[1])
                    destino = int(partes[2])
                    custo_transporte = int(partes[3])
                    grafo.adicionar_aresta(origem, destino, custo_transporte)

                elif secao == "arcos_nao_obrigatorios":
                    origem = int(partes[1])
                    destino = int(partes[2])
                    custo_transporte = int(partes[3])
                    grafo.adicionar_arco(origem, destino, custo_transporte)

            except (ValueError, IndexError) as e:
                print(f"Linha ignorada: {linha} (Erro: {str(e)})")
                continue

    return grafo
