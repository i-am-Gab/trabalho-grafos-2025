def floyd_warshall(graph):
    vertices = sorted(graph.vertices)
    num_vertices = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}

    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    pred = [[None] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        dist[i][i] = 0

    connections = (
        graph.arcs +
        [(u, v, t) for u, v, t, *_ in graph.required_arcs] +
        graph.edges +
        [(u, v, t) for u, v, t, *_ in graph.required_edges]
    )

    for u, v, cost in connections:
        i, j = index[u], index[v]
        if dist[i][j] > cost:
            dist[i][j] = cost
            pred[i][j] = i

        is_undirected = (
            (u, v, cost) in graph.edges or
            (v, u, cost) in graph.edges or
            any(((u == x and v == y) or (v == x and u == y)) for x, y, t, *_ in graph.required_edges if t == cost)
        )
        if is_undirected and dist[j][i] > cost:
            dist[j][i] = cost
            pred[j][i] = j

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred, index


def reconstruct_path(u, v, pred, index):
    path = []
    i, j = index[u], index[v]
    if pred[i][j] is None:
        return []

    while j != i:
        path.append(j)
        j = pred[i][j]
    path.append(i)
    path.reverse()
    return path
