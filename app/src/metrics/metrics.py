def calcular_metricas(grafo, distancias, pred, indice):
    metricas = {}
    
    # Identifica o tipo de grafo
    tipo = identificar_tipo_grafo(grafo)
    metricas["tipo"] = tipo

    # Métricas básicas
    metricas.update(calcular_metricas_basicas(grafo))
    
    # Densidade do grafo
    n = len(grafo.vertices)
    metricas["densidade"] = calcular_densidade(n, metricas["num_arestas"], metricas["num_arcos"], tipo)
    
    # Grau dos vértices
    grau, grau_minimo, grau_maximo = calcular_grau(grafo)
    metricas["grau_minimo"] = grau_minimo
    metricas["grau_maximo"] = grau_maximo
    
    # Intermediação
    vertices = sorted(grafo.vertices)
    metricas["intermediacao"] = calcular_intermediacao(vertices, distancias, pred, indice)
    
    # Caminho médio e diâmetro
    caminho_medio, diametro = calcular_caminhos_e_diametro(vertices, distancias)
    metricas["caminho_medio"] = caminho_medio
    metricas["diametro"] = diametro

    return metricas

def identificar_tipo_grafo(grafo):
    tem_arestas = len(grafo.arestas) > 0 or len(grafo.arestas_obrigatorias) > 0
    tem_arcos = len(grafo.arcos) > 0 or len(grafo.arcos_obrigatorios) > 0

    if tem_arestas and tem_arcos:
        return 'misto'
    elif tem_arcos:
        return 'direcionado'
    elif tem_arestas:
        return 'nao_direcionado'
    else:
        return 'vazio'

def calcular_metricas_basicas(grafo):
    metricas = {}
    metricas["num_vertices"] = len(grafo.vertices)
    metricas["num_arestas"] = len(grafo.arestas) + len(grafo.arestas_obrigatorias)
    metricas["num_arcos"] = len(grafo.arcos) + len(grafo.arcos_obrigatorios)
    metricas["num_nos_obrigatorios"] = len(grafo.nos_obrigatorios)
    metricas["num_arestas_obrigatorias"] = len(grafo.arestas_obrigatorias)
    metricas["num_arcos_obrigatorios"] = len(grafo.arcos_obrigatorios)
    return metricas

def calcular_densidade(n, num_arestas, num_arcos, tipo):
    if tipo == 'nao_direcionado':
        max_conexoes = n * (n - 1) / 2
        total_conexoes = num_arestas
    elif tipo == 'direcionado':
        max_conexoes = n * (n - 1)
        total_conexoes = num_arcos
    elif tipo == 'misto':
        max_conexoes = n * (n - 1)
        total_conexoes = num_arestas + num_arcos
    else:
        return 0 

    return total_conexoes / max_conexoes if max_conexoes > 0 else 0


def calcular_grau(grafo):
    # Inicializa o grau 0 para todos os vértices
    grau = {v: 0 for v in grafo.vertices}

    # Unifica arestas e arestas obrigatórias (usando as três primeiras posições para evitar duplicatas)
    todas_arestas = set(tuple(aresta[:3]) for aresta in grafo.arestas + grafo.arestas_obrigatorias)
    # Unifica arcos e arcos obrigatórios
    todos_arcos = set(tuple(arc[:3]) for arc in grafo.arcos + grafo.arcos_obrigatorios)

    # Arestas (não direcionadas): contam para ambos os vértices
    for u, v, _ in todas_arestas:
        grau[u] += 1
        grau[v] += 1

    # Arcos (direcionados): contam para origem e destino
    for u, v, _ in todos_arcos:
        grau[u] += 1  # saída
        grau[v] += 1  # entrada

    grau_minimo = min(grau.values())
    grau_maximo = max(grau.values())
    return grau, grau_minimo, grau_maximo

def calcular_intermediacao(vertices, distancias, pred_matrix, indice):
    intermediacao = {v: 0 for v in vertices}

    # Percorre todos os pares (s, t)
    for s in vertices:
        for t in vertices:
            if s == t:
                continue

            # Obtém os índices correspondentes
            s_idx = indice[s]
            t_idx = indice[t]
            
            # Verifica se há caminho entre s e t
            if distancias[s_idx][t_idx] == float('inf'):
                continue
            
            # Reconstrói o caminho a partir da matriz de predecessores.
            # Começamos a partir de t e retrocedemos até s.
            caminho = []
            atual = t_idx
            # Enquanto houver predecessor e não chegamos em s
            while pred_matrix[s_idx][atual] is not None and atual != s_idx:
                # Obtém o predecessor de 'atual'
                pred = pred_matrix[s_idx][atual]
                caminho.append(pred)
                atual = pred

            # Cada vértice que não seja s ou t é considerado intermediário
            for v_idx in caminho:
                if v_idx != s_idx and v_idx != t_idx:
                    v = vertices[v_idx]
                    intermediacao[v] += 1

    return intermediacao

def calcular_caminhos_e_diametro(vertices, distancias):
    total = 0
    count = 0
    diametro = 0
    n = len(vertices)

    for i in range(n):
        for j in range(n):
            if i != j:
                d = distancias[i][j]
                if d != float('inf'):
                    total += d
                    count += 1
                    diametro = max(diametro, d)

    caminho_medio = total / count if count > 0 else 0
    return caminho_medio, diametro

