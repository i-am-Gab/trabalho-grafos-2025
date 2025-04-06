def print_matrices(dist, pred, index):
    vertices = sorted(index.keys())
    num_vertices = len(vertices)

    print("\n=== Matriz de Distâncias (completa) ===")
    print("     " + " ".join(f"{v:>5}" for v in vertices))
    for i in range(num_vertices):
        row = [f"{dist[i][j]:>5.1f}" if dist[i][j] != float('inf') else "  inf" for j in range(num_vertices)]
        print(f"{vertices[i]:>3} " + " ".join(row))

    print("\n=== Matriz de Predecessores (completa) ===")
    print("     " + " ".join(f"{v:>5}" for v in vertices))
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            if pred[i][j] is not None:
                row.append(f"{vertices[pred[i][j]]:>5}")
            else:
                row.append(" None" if i != j else "   - ")
        print(f"{vertices[i]:>3} " + " ".join(row))