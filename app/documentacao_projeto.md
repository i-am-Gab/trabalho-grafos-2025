
# Documentação do Projeto

Este projeto implementa funcionalidades para manipulação de grafos mistos, incluindo carregamento de instâncias, cálculo de métricas, algoritmos de caminho mínimo e exibição de resultados. Abaixo está a descrição de cada arquivo do projeto.

---

## Arquivo: main.ipynb

### Descrição
Este notebook é o ponto de entrada principal do projeto. Ele utiliza as funções e classes implementadas nos outros arquivos para carregar uma instância de grafo, calcular métricas e exibir os resultados.

### Estrutura
1. **Célula 1**: Importa os módulos necessários:
   - `load_instance` (de `loader.py`)
   - `floyd_warshall` (de `algorithms.py`)
   - `calculate_metrics` (de `metrics.py`)
   - `print_matrices` (de `utils.py`)
   - `metric_labels` (de `labels.py`)

2. **Célula 2**: Executa o fluxo principal:
   - Carrega o grafo a partir de um arquivo.
   - Calcula as distâncias e predecessores usando o algoritmo de Floyd-Warshall.
   - Calcula métricas do grafo.
   - Exibe as métricas calculadas.

3. **Célula 3**: Exibe as matrizes de distâncias e predecessores.

---

## Arquivo: loader.py

### Descrição
Contém a função responsável por carregar uma instância de grafo a partir de um arquivo.

### Funções
- **`load_instance(file_path)`**:
  - Carrega uma instância de grafo a partir de um arquivo e retorna um objeto `Multigraph`.
  - **Parâmetros**: `file_path` (str) – Caminho para o arquivo de instância.
  - **Retorno**: Objeto `Multigraph`.

---

## Arquivo: algorithms.py

### Descrição
Implementa algoritmos para manipulação de grafos.

### Funções
- **`floyd_warshall(graph)`**:
  - Calcula a matriz de distâncias e predecessores para todos os pares de vértices usando o algoritmo de Floyd-Warshall.
  - **Parâmetros**: `graph` (Multigraph) – Grafo para o qual as distâncias serão calculadas.
  - **Retorno**: `dist` (list), `pred` (list), `index` (dict).

---

## Arquivo: graph.py

### Descrição
Define a classe `Multigraph`, que representa um grafo misto.

### Classes
- **`Multigraph`**:
  - Representa um grafo misto com suporte a nós, arestas e arcos obrigatórios e não obrigatórios.
  - **Atributos**:
    - `vertices`: Conjunto de vértices.
    - `edges`: Lista de arestas não obrigatórias.
    - `arcs`: Lista de arcos não obrigatórios.
    - `required_nodes`: Lista de nós obrigatórios.
    - `required_edges`: Lista de arestas obrigatórias.
    - `required_arcs`: Lista de arcos obrigatórios.

---

## Arquivo: labels.py

### Descrição
Contém rótulos descritivos para as métricas calculadas.

### Variáveis
- **`metric_labels`**:
  - Dicionário que mapeia as chaves das métricas para descrições legíveis.

---

## Arquivo: metrics.py

### Descrição
Implementa funções para calcular métricas de grafos.

### Funções
- **`calculate_metrics(graph, dist, pred, index)`**:
  - Calcula métricas do grafo, como número de vértices, densidade, grau mínimo/máximo e centralidade de intermediação.
  - **Parâmetros**:
    - `graph` (Multigraph): Grafo para o qual as métricas serão calculadas.
    - `dist` (list): Matriz de distâncias.
    - `pred` (list): Matriz de predecessores.
    - `index` (dict): Mapeamento de vértices para índices.
  - **Retorno**: `dict` contendo as métricas calculadas.

---

## Arquivo: utils.py

### Descrição
Contém funções auxiliares para exibição de resultados.

### Funções
- **`print_matrices(dist, pred, index, sample_size=5)`**:
  - Exibe as matrizes de distâncias e predecessores para uma amostra de vértices.
  - **Parâmetros**:
    - `dist` (list): Matriz de distâncias.
    - `pred` (list): Matriz de predecessores.
    - `index` (dict): Mapeamento de vértices para índices.
    - `sample_size` (int): Número de vértices a serem exibidos (padrão: 5).

---
