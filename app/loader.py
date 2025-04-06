from graph import Multigraph

def load_instance(file_path):
    graph = Multigraph()
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

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
