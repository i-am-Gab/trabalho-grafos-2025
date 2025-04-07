def floyd_warshall(grafo):
    vertices = sorted(grafo.vertices)
    num_vertices = len(vertices)
    indice = {v: i for i, v in enumerate(vertices)}

    distancias = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    predecessores = [[None] * num_vertices for _ in range(num_vertices)]

    # Inicializa as distâncias de cada vértice para ele mesmo com 0
    for i in range(num_vertices):
        distancias[i][i] = 0

    # Junta todas as conexões (arestas e arcos)
    ligacoes = (
        grafo.arcos +
        [(u, v, t) for u, v, t, *_ in grafo.arcos_obrigatorios] +
        grafo.arestas +
        [(u, v, t) for u, v, t, *_ in grafo.arestas_obrigatorias]
    )

    for u, v, custo in ligacoes:
        i, j = indice[u], indice[v]
        if distancias[i][j] > custo:
            distancias[i][j] = custo
            predecessores[i][j] = i

        # Verifica se é uma aresta não direcionada
        nao_direcionado = (
            (u, v, custo) in grafo.arestas or
            (v, u, custo) in grafo.arestas or
            any(((u == x and v == y) or (v == x and u == y)) for x, y, t, *_ in grafo.arestas_obrigatorias if t == custo)
        )
        if nao_direcionado and distancias[j][i] > custo:
            distancias[j][i] = custo
            predecessores[j][i] = j

    # Algoritmo de Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
                    predecessores[i][j] = predecessores[k][j]

    return distancias, predecessores, indice


def reconstruir_caminho(u, v, predecessores, indice):
    caminho = []
    i, j = indice[u], indice[v]
    if predecessores[i][j] is None:
        return []

    while j != i:
        caminho.append(j)
        j = predecessores[i][j]
    caminho.append(i)
    caminho.reverse()
    return caminho
