## 📁 Estrutura do Projeto 1

```bash
📂app
 ┣ 📂src
 ┃ ┣ 📂algorithms
 ┃ ┃ ┗ 📜algorithms.py
 ┃ ┣ 📂graph
 ┃ ┃ ┗ 📜graph.py
 ┃ ┣ 📂lang
 ┃ ┃ ┗ 📜labels.py
 ┃ ┣ 📂loader
 ┃ ┃ ┗ 📜loader.py
 ┃ ┣ 📂metrics
 ┃ ┃ ┗ 📜metrics.py
 ┃ ┗ 📂utils
 ┃   ┗ 📜utils.py
 ┃ 
 ┣ 📂storage
 ┗ ┗ 📜Arquivos disponibilizados para teste.
  
📜main.ipynb
📜README.md

```

---

## 🔧 Como Usar

### 1. Formato do Arquivo de Entrada
O arquivo (ex.: BHW1.dat) deve seguir um formato compatível com instâncias CARP, contendo:

- Nós obrigatórios (ReN.)
  
- Arestas obrigatórias (ReE.)
 
- Arcos obrigatórios (ReA.)

- ARC origem destino 

- Custo travessia 

- Demanda 

- Custo serviço  

- Arestas/arcos não obrigatórios (EDGE/ARC sem demanda)

### 2. Execução

Execute o arquivo main.ipynb localizado dentro de 📂etapa_01

Insira o nome do arquivo .dat que será lido pelo programa.
 - O arquivo deve estar dentro de 📂storage;
 - O arquivo deve estar formatado de acordo com os demais arquivos presentes na pasta. 

Saída esperada:

=== Métricas do Grafo ===
- Número total de vértices
- Número total de arestas
- Número total de arcos
- Número de nós obrigatórios
- Número de arestas obrigatórias
- Número de arcos obrigatórios
- Densidade do grafo
- Grau mínimo
- Grau máximo
- Intermediação (Betweenness Centrality)
- Caminho médio
- Diâmetro

=== Matriz de Distâncias (completa) ===

=== Matriz de Predecessores (completa) ===