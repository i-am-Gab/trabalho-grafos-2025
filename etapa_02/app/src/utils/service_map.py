def mapear_servicos_para_id_servico(grafo):
    id_servico = {}
    contador = 1

    for no, _, _ in grafo.nos_obrigatorios:
        id_servico[(no, no)] = contador
        contador += 1

    for u, v, *_ in grafo.arestas_obrigatorias:
        id_servico[(u, v)] = contador
        id_servico[(v, u)] = contador
        contador += 1

    for u, v, *_ in grafo.arcos_obrigatorios:
        id_servico[(u, v)] = contador
        contador += 1

    return id_servico