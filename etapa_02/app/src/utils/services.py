def listar_servicos(grafo):
    servicos = []

    for no, demanda, custo_s in grafo.nos_obrigatorios:
        servicos.append({
            'tipo': 'no',
            'origem': no,
            'destino': no,
            'demanda': demanda,
            'custo_s': custo_s
        })

    for origem, destino, _, demanda, custo_s in grafo.arestas_obrigatorias:
        servicos.append({
            'tipo': 'aresta',
            'origem': origem,
            'destino': destino,
            'demanda': demanda,
            'custo_s': custo_s
        })

    for origem, destino, _, demanda, custo_s in grafo.arcos_obrigatorios:
        servicos.append({
            'tipo': 'arco',
            'origem': origem,
            'destino': destino,
            'demanda': demanda,
            'custo_s': custo_s
        })

    return servicos