
# Trabalho Prático - Grafos - Etapa 1

📌 Visão Geral

Este projeto implementa uma estrutura de grafo misto (contendo arestas não direcionadas e arcos direcionados) para análise de problemas de roteamento, como o Capacitated Arc Routing Problem (CARP). Ele inclui:  
- Carregamento de instâncias a partir de arquivos de dados  
- Cálculo de caminhos mínimos entre todos os pares de nós (Floyd-Warshall)  
- Métricas de análise do grafo (densidade, centralidade, diâmetro, etc.)  
- Visualização de resultados (matriz de distâncias, predecessores e exemplos de caminhos)




## 📋 Requisitos  
- Python 3.8+  
- Nenhuma dependência externa (usa apenas bibliotecas padrão) 

## 🔧 Como Usar

#### 1. Formato do Arquivo de Entrada
O arquivo (ex.: BHW1.dat) deve seguir um formato compatível com instâncias CARP, contendo:

- Nós obrigatórios (ReN.)
  
- Arestas obrigatórias (ReE.)
 
- Arcos obrigatórios (ReA.)

- ARC origem destino 

- Custo travessia 

- Demanda 

- Custo serviço  

- Arestas/arcos não obrigatórios (EDGE/ARC sem demanda)

#### 2. Execução

Saída esperada:

- Métricas do grafo (número de vértices, arestas, densidade, etc.)

- Exemplo de caminho mínimo entre dois nós

- Matrizes de distância e predecessores (amostra)


## Autores

- [@GabrielAguiar](https://https://github.com/i-am-Gab)
- [@ViniciusOliveira](https://github.com/viniciusdev7)
