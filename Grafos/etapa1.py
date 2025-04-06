import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.MultiDiGraph()  # Permite múltiplas arestas direcionadas entre pares de nós

    # Adiciona nós
    for v in graph.vertices:
        G.add_node(v)

    # Adiciona arestas não direcionadas (edges e required_edges)
    for u, v, _ in graph.edges:
        G.add_edge(u, v, color='black')  # Aresta normal (bidirecional para visualização)
        G.add_edge(v, u, color='black')
    for u, v, *_ in graph.required_edges:
        G.add_edge(u, v, color='blue')
        G.add_edge(v, u, color='blue')

    # Adiciona arcos direcionados (arcs e required_arcs)
    for u, v, _ in graph.arcs:
        G.add_edge(u, v, color='gray')
    for u, v, *_ in graph.required_arcs:
        G.add_edge(u, v, color='red')

    # Define layout dos nós
    pos = nx.spring_layout(G, seed=42)

    # Desenha nós e rótulos
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Desenha arestas com curvatura para diferenciar múltiplas
    for u, v, key, data in G.edges(keys=True, data=True):
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(u, v)],
            edge_color=data['color'],
            connectionstyle='arc3,rad=0.2',  # Curvatura para evitar sobreposição
            arrows=True,
            arrowstyle='-|>',
            min_source_margin=15,
            min_target_margin=15
        )

    plt.title("Visualização do Grafo com MultiDiGraph")
    plt.axis('off')
    plt.show()
    
""" Esta classe representa um grafo misto """
class Multigraph:
    def __init__(self):
        self.depot = None
        self.capacity = None
        self.vertices = set()
        self.edges = []
        self.arcs = []
        self.required_nodes = []
        self.required_edges = []
        self.required_arcs = []


""" Carrega o arquivo de instância e retorna um objeto Multigraph """
def load_instance(file_path):
    graph = Multigraph()
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    """Inicializa section como None para controlar a seção atual do arquivo"""
    section = None
    for line in lines:
        if line.startswith(("Name", "Optimal", "#", "the data is")):
            continue
            
        if "ReN." in line:
            section = "required_nodes"
            continue
        elif "ReE." in line:
            section = "required_edges"
            continue
        elif "EDGE" in line:
            section = "non_required_edges"
            continue
        elif "ReA." in line:
            section = "required_arcs"
            continue
        elif "ARC" in line:
            section = "non_required_arcs"
            continue

        """Detecta marcadores de seção no arquivo e atualiza a seção atual. Se estiver em uma seção, divide a linha em partes"""    
        if section:
            parts = line.split()
            try:
                if section == "required_nodes":
                    node = int(parts[0].replace("N", ""))
                    demand, s_cost = map(int, parts[1:3])
                    graph.required_nodes.append((node, demand, s_cost))
                    graph.vertices.add(node)
                    
                elif section == "required_edges":
                    from_node = int(parts[1])
                    to_node = int(parts[2])
                    t_cost = int(parts[3])
                    demand = int(parts[4])
                    s_cost = int(parts[5])
                    graph.required_edges.append((from_node, to_node, t_cost, demand, s_cost))
                    graph.vertices.update([from_node, to_node])
                    
                elif section == "required_arcs":
                    from_node = int(parts[1])
                    to_node = int(parts[2])
                    t_cost = int(parts[3])
                    demand = int(parts[4])
                    s_cost = int(parts[5])
                    graph.required_arcs.append((from_node, to_node, t_cost, demand, s_cost))
                    graph.vertices.update([from_node, to_node])
                    
                elif section == "non_required_edges":
                    from_node = int(parts[1])
                    to_node = int(parts[2])
                    t_cost = int(parts[3])
                    graph.edges.append((from_node, to_node, t_cost))
                    graph.vertices.update([from_node, to_node])
                    
                elif section == "non_required_arcs":
                    from_node = int(parts[1])
                    to_node = int(parts[2])
                    t_cost = int(parts[3])
                    graph.arcs.append((from_node, to_node, t_cost))
                    graph.vertices.update([from_node, to_node])
                    
            except (ValueError, IndexError) as e:
                print(f"Linha ignorada: {line} (Erro: {str(e)})")
                continue
    
    return graph


"""Calcula a matriz de distâncias e predecessores para todos os pares de nós."""
def floyd_warshall(graph):
    vertices = sorted(graph.vertices)
    num_vertices = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    
    # Inicializa matriz de distâncias e predecessores
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    pred = [[None] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        dist[i][i] = 0
    
    # Preenche distâncias diretas e predecessores iniciais
    connections = (
        graph.arcs +
        [(u, v, t) for u, v, t, *_ in graph.required_arcs] +
        graph.edges +
        [(u, v, t) for u, v, t, *_ in graph.required_edges]
    )
    """Cria lista de todas as conexões (arcos e arestas, obrigatórios e não obrigatórios)"""
    for u, v, cost in connections:
        i, j = index[u], index[v]
        if dist[i][j] > cost:
            dist[i][j] = cost
            pred[i][j] = i  # Predecessor de j no caminho i->j é i
        
        """Para cada conexão, atualiza a distância e predecessor se for menor que o valor atual"""    
        # Se for aresta não direcionada, adiciona inverso
        is_undirected = (
            (u, v, cost) in graph.edges or
            (v, u, cost) in graph.edges or
            any(((u == x and v == y) or (v == x and u == y)) for x, y, t, *_ in graph.required_edges if t == cost)
        )
        if is_undirected and dist[j][i] > cost:
            dist[j][i] = cost
            pred[j][i] = j
    
    """Implementa o núcleo do algoritmo de Floyd-Warshall, verificando se passar pelo vértice k reduz a distância entre i e j"""
    # Algoritmo de Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]  # Atualiza predecessor
    
    return dist, pred, index


"""Reconstrói o caminho mais curto entre dois vértices:"""
def reconstruct_path(u, v, pred, index):
    path = []
    i, j = index[u], index[v]
    if pred[i][j] is None:
        return []  # Não há caminho
    
    while j != i:
        path.append(j)
        j = pred[i][j]
    path.append(i)
    path.reverse()
    
    return path


"""Calcula todas as métricas requeridas."""
def calculate_metrics(graph, dist, pred, index):
    metrics = {}
    vertices = sorted(graph.vertices)

    # 1–6: Quantidades básicas
    metrics["num_vertices"] = len(graph.vertices)
    metrics["num_edges"] = len(graph.edges) + len(graph.required_edges)
    metrics["num_arcs"] = len(graph.arcs) + len(graph.required_arcs)
    metrics["num_required_nodes"] = len(graph.required_nodes)
    metrics["num_required_edges"] = len(graph.required_edges)
    metrics["num_required_arcs"] = len(graph.required_arcs)
    
    # 7. Densidade (aproximada para arestas não direcionadas)
    n = len(graph.vertices)
    num_possible_undirected = n * (n - 1) / 2
    metrics["density"] = metrics["num_edges"] / num_possible_undirected if num_possible_undirected else 0

    # 9–10: Grau mínimo e máximo
    degree = {v: 0 for v in graph.vertices}
    for u, v, _ in graph.edges + [(u, v, _) for u, v, *_ in graph.required_edges]:
        degree[u] += 1
        degree[v] += 1
    for u, v, _ in graph.arcs + [(u, v, _) for u, v, *_ in graph.required_arcs]:
        degree[u] += 1  # Apenas origem para arcos direcionados
    metrics["min_degree"] = min(degree.values())
    metrics["max_degree"] = max(degree.values())

    # 11. Intermediação (versão simplificada)
    betweenness = {v: 0 for v in graph.vertices}
    for s in vertices:
        for t in vertices:
            if s != t and dist[index[s]][index[t]] != float('inf'):
                for v in vertices:
                    if v != s and v != t:
                        if dist[index[s]][index[v]] + dist[index[v]][index[t]] == dist[index[s]][index[t]]:
                            betweenness[v] += 1
    metrics["betweenness"] = betweenness

    # 12–13: Caminho médio e diâmetro
    total = 0
    count = 0
    diameter = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            d = dist[i][j]
            if d != float('inf'):
                total += d
                count += 1
                if d > diameter:
                    diameter = d
    metrics["avg_path"] = total / count if count > 0 else 0
    metrics["diameter"] = diameter

    return metrics


"""Exibe as matrizes de distâncias e predecessores (amostra dos primeiros 'sample_size' nós)."""
def print_matrices(dist, pred, index, sample_size=5):
    vertices = sorted(index.keys())
    sample_nodes = vertices[:sample_size]
    sample_indices = [index[v] for v in sample_nodes]

    # Matriz de Distâncias
    print("\n=== Matriz de Distâncias (amostra) ===")
    print("    " + " ".join(f"{v:>5}" for v in sample_nodes))
    for i in sample_indices:
        row = [f"{dist[i][j]:>5.1f}" if dist[i][j] != float('inf') else "  inf" for j in sample_indices]
        print(f"{vertices[i]:>3} " + " ".join(row))

    # Matriz de Predecessores
    print("\n=== Matriz de Predecessores (amostra) ===")
    print("    " + " ".join(f"{v:>5}" for v in sample_nodes))
    for i in sample_indices:
        row = []
        for j in sample_indices:
            if pred[i][j] is not None:
                row.append(f"{vertices[pred[i][j]]:>5}")
            else:
                row.append("  None" if i != j else "    -")  # Diagonal principal
        print(f"{vertices[i]:>3} " + " ".join(row))

def main():
    try:
        graph = load_instance("mggdb_0.25_6.dat")
        dist, pred, index = floyd_warshall(graph)
        metrics = calculate_metrics(graph, dist, pred, index)
        
        metric_labels = {
            "num_vertices": "Número total de vértices",
            "num_edges": "Número total de arestas",
            "num_arcs": "Número total de arcos",
            "num_required_nodes": "Número de nós obrigatórios",
            "num_required_edges": "Número de arestas obrigatórias",
            "num_required_arcs": "Número de arcos obrigatórios",
            "betweenness": "Intermediação (Betweenness Centrality)",
            "density": "Densidade do grafo",
            "min_degree": "Grau mínimo",
            "max_degree": "Grau máximo",
            "avg_path": "Caminho médio",
        }

        print("=== Métricas do Grafo ===")
        for key, value in metrics.items():
            label = metric_labels.get(key, key)  # Usa a frase personalizada, ou a chave como fallback

            if key == "betweenness":
                print(f"{label}:")
                for node, bc in sorted(value.items()):
                    print(f"  Nó {node}: {bc:.4f}")
            elif key == "example_path":
                print(f"\n{label} (entre {value['from']} e {value['to']}):")
                print(" -> ".join(map(str, value["path"])))
            else:
                print(f"{label}: {value:.2f}" if isinstance(value, float) else f"{label}: {value}")


        # Exibe as matrizes (amostra dos primeiros 5 nós)
        print_matrices(dist, pred, index, sample_size=5)
        
        visualize_graph(graph)  # Visualiza o grafo após calcular as métricas
                
    except FileNotFoundError:
        print("Erro: Arquivo BHW1.dat não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        

if __name__ == "__main__":
    main()