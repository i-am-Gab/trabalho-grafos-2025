
# Trabalho Prático - Grafos - Etapa 1

📌 Visão Geral

Este projeto implementa uma estrutura de grafo misto (contendo arestas não direcionadas e arcos direcionados) para análise de problemas de roteamento, como o Capacitated Arc Routing Problem (CARP). Ele inclui:  
- Carregamento de instâncias a partir de arquivos de dados  
- Cálculo de caminhos mínimos entre todos os pares de nós (Floyd-Warshall)  
- Métricas de análise do grafo (densidade, centralidade, diâmetro, etc.)  
- Visualização de resultados (matriz de distâncias, predecessores e exemplos de caminhos)

## 📋 Requisitos  
- Python 3.12+  
- Nenhuma dependência externa (usa apenas bibliotecas padrão) 

## 🗂️ Estrutra dos arquivos

📦app
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
 ┃ ┣ 📂utils
 ┃ ┃ ┗ 📜utils.py
 ┃ ┗ 📜main.ipynb
 ┣ 📂storage
 ┃ ┣ 📜BHW1.dat
 ┃ ┣ 📜BHW10.dat
 ┃ ┣ 📜BHW2.dat
 ┃ ┣ 📜BHW3.dat
 ┃ ┣ 📜BHW4.dat
 ┃ ┣ 📜BHW5.dat
 ┃ ┣ 📜BHW6.dat
 ┃ ┣ 📜BHW7.dat
 ┃ ┣ 📜BHW8.dat
 ┃ ┣ 📜BHW9.dat
 ┃ ┣ 📜CBMix11.dat
 ┃ ┣ 📜CBMix12.dat
 ┃ ┣ 📜CBMix13.dat
 ┃ ┣ 📜CBMix14.dat
 ┃ ┣ 📜CBMix15.dat
 ┃ ┣ 📜CBMix16.dat
 ┃ ┣ 📜CBMix17.dat
 ┃ ┣ 📜CBMix18.dat
 ┃ ┣ 📜CBMix19.dat
 ┃ ┣ 📜CBMix20.dat
 ┃ ┣ 📜DI-NEARP-n240-Q16k.dat
 ┃ ┣ 📜DI-NEARP-n240-Q2k.dat
 ┃ ┣ 📜DI-NEARP-n240-Q4k.dat
 ┃ ┣ 📜DI-NEARP-n240-Q8k.dat
 ┃ ┣ 📜DI-NEARP-n422-Q16k.dat
 ┃ ┣ 📜DI-NEARP-n422-Q2k.dat
 ┃ ┣ 📜DI-NEARP-n422-Q4k.dat
 ┃ ┣ 📜DI-NEARP-n422-Q8k.dat
 ┃ ┣ 📜DI-NEARP-n442-Q2k.dat
 ┃ ┣ 📜DI-NEARP-n442-Q4k.dat
 ┃ ┣ 📜mggdb_0.25_1.dat
 ┃ ┣ 📜mggdb_0.25_10.dat
 ┃ ┣ 📜mggdb_0.25_2.dat
 ┃ ┣ 📜mggdb_0.25_3.dat
 ┃ ┣ 📜mggdb_0.25_4.dat
 ┃ ┣ 📜mggdb_0.25_5.dat
 ┃ ┣ 📜mggdb_0.25_6.dat
 ┃ ┣ 📜mggdb_0.25_7.dat
 ┃ ┣ 📜mggdb_0.25_8.dat
 ┃ ┣ 📜mggdb_0.25_9.dat
 ┃ ┣ 📜mgval_0.50_10A.dat
 ┃ ┣ 📜mgval_0.50_10B.dat
 ┃ ┣ 📜mgval_0.50_10C.dat
 ┃ ┣ 📜mgval_0.50_10D.dat
 ┃ ┣ 📜mgval_0.50_8B.dat
 ┃ ┣ 📜mgval_0.50_8C.dat
 ┃ ┣ 📜mgval_0.50_9A.dat
 ┃ ┣ 📜mgval_0.50_9B.dat
 ┃ ┣ 📜mgval_0.50_9C.dat
 ┃ ┗ 📜mgval_0.50_9D.dat
 ┣ 📂__pycache__
 ┃ ┣ 📜algorithms.cpython-312.pyc
 ┃ ┣ 📜graph.cpython-312.pyc
 ┃ ┣ 📜labels.cpython-312.pyc
 ┃ ┣ 📜loader.cpython-312.pyc
 ┃ ┣ 📜metrics.cpython-312.pyc
 ┃ ┗ 📜utils.cpython-312.pyc
 ┗ 📜documentacao_projeto.md
📜README.md

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
