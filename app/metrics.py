def calculate_metrics(graph, dist, pred, index):
    metrics = {}
    vertices = sorted(graph.vertices)

    metrics["num_vertices"] = len(graph.vertices)
    metrics["num_edges"] = len(graph.edges) + len(graph.required_edges)
    metrics["num_arcs"] = len(graph.arcs) + len(graph.required_arcs)
    metrics["num_required_nodes"] = len(graph.required_nodes)
    metrics["num_required_edges"] = len(graph.required_edges)
    metrics["num_required_arcs"] = len(graph.required_arcs)

    n = len(graph.vertices)
    
    # Calula a densidade do grafo
    max_connections = n * (n - 1)
    total_connections = (2 *  metrics["num_edges"]) +  metrics["num_arcs"] 
    total_connections = metrics["num_edges"] +  metrics["num_arcs"] 
    metrics["density"] = total_connections / max_connections if max_connections > 0 else 0
    
   # Inicializa grau 0 para todos os vértices
    degree = {v: 0 for v in graph.vertices}

    # Unifica arestas e arestas obrigatórias sem duplicar
    all_edges = set(tuple(edge[:3]) for edge in graph.edges + graph.required_edges)

    # Unifica arcos e arcos obrigatórios sem duplicar
    all_arcs = set(tuple(arc[:3]) for arc in graph.arcs + graph.required_arcs)

    # Arestas (não direcionadas): contam para u e v
    for u, v, _ in all_edges:
        degree[u] += 1
        degree[v] += 1

    # Arcos (direcionados): contam para origem e destino (grau total)
    for u, v, _ in all_arcs:
        degree[u] += 1  # saída
        degree[v] += 1  # entrada

    # Armazena grau mínimo e máximo
    metrics["min_degree"] = min(degree.values())
    metrics["max_degree"] = max(degree.values())
    
    #Calcula as intermediações
    betweenness = {v: 0 for v in graph.vertices}
    for s in vertices:
        for t in vertices:
            if s != t and dist[index[s]][index[t]] != float('inf'):
                for v in vertices:
                    if v != s and v != t:
                        if dist[index[s]][index[v]] + dist[index[v]][index[t]] == dist[index[s]][index[t]]:
                            betweenness[v] += 1
    metrics["betweenness"] = betweenness

    total = 0
    count = 0
    diameter = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            d = dist[i][j]
            if d != float('inf'):
                total += d
                count += 1
                diameter = max(diameter, d)            
    metrics["avg_path"] = total / count if count > 0 else 0 #Calcula a média dos caminhos
    metrics["diameter"] = diameter #Calcula o diâmetro do grafo

    return metrics
