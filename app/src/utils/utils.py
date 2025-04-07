def imprimir_matrizes(distancias, predecessores, indice):
    vertices = sorted(indice.keys())
    num_vertices = len(vertices)

    print("\n=== Matriz de Distâncias (completa) ===")
    print("     " + " ".join(f"{v:>5}" for v in vertices))
    for i in range(num_vertices):
        linha = [f"{distancias[i][j]:>5.1f}" if distancias[i][j] != float('inf') else "  inf" for j in range(num_vertices)]
        print(f"{vertices[i]:>3} " + " ".join(linha))

    print("\n=== Matriz de Predecessores (completa) ===")
    print("     " + " ".join(f"{v:>5}" for v in vertices))
    for i in range(num_vertices):
        linha = []
        for j in range(num_vertices):
            if predecessores[i][j] is not None:
                linha.append(f"{vertices[predecessores[i][j]]:>5}")
            else:
                linha.append(" None" if i != j else "   - ")
        print(f"{vertices[i]:>3} " + " ".join(linha))
