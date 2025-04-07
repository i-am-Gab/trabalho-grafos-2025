# Documentação do Projeto

## Arquivo: main.ipynb
### Descrição
Notebook principal que integra as funcionalidades do projeto para carregar instâncias de grafos, calcular métricas e exibir resultados.

### Estrutura
- **Célula 1**: Importa os módulos necessários.
- **Célula 2**: Executa o fluxo principal (carrega o grafo, calcula métricas e exibe resultados).
- **Célula 3**: Exibe as matrizes de distâncias e predecessores.

## Arquivo: loader.py
### Descrição
Carrega uma instância de grafo a partir de um arquivo no formato especificado.

### Funções
- **`carregar_instancia(caminho_arquivo)`**: Lê o arquivo e constrói um objeto `Multigraph`.

## Arquivo: graph.py
### Descrição
Define a classe `Multigraph`, que representa um grafo misto com suporte a nós, arestas e arcos obrigatórios e não obrigatórios.

### Classes
- **`Multigraph`**: Classe principal para manipulação de grafos.

## Arquivo: algorithms.py
### Descrição
Implementa algoritmos para manipulação de grafos.

### Funções
- **`floyd_warshall(grafo)`**: Calcula as matrizes de distâncias e predecessores.
- **`reconstruir_caminho(u, v, predecessores, indice)`**: Reconstrói o caminho mínimo entre dois vértices.

## Arquivo: metrics.py
### Descrição
Calcula métricas de grafos, como densidade, grau, intermediação, caminho médio e diâmetro.

### Funções
- **`calcular_metricas(grafo, distancias, pred, indice)`**: Calcula diversas métricas do grafo.

## Arquivo: utils.py
### Descrição
Funções auxiliares para exibição de resultados.

### Funções
- **`imprimir_matrizes(distancias, predecessores, indice)`**: Exibe as matrizes de distâncias e predecessores.

## Arquivo: labels.py
### Descrição
Define rótulos descritivos para as métricas calculadas.

### Variáveis
- **`metric_labels`**: Dicionário que mapeia as métricas para descrições legíveis.

