# 🚚 GCC218 - Trabalho Prático: Análise de Grafos em Problemas Logísticos

> Projeto desenvolvido para o Trabalho Prático Final das disciplinas **GCC218 - Grafos e Suas Aplicações** da Universidade Federal de Lavras.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/Licença-Educacional-green" alt="Licença Educacional">
</div>

## 👨‍🏫 Orientador
Prof. Mayron César O. Moreira
Universidade Federal de Lavras - UFLA
2025

## 📚 Sobre o Projeto

Este projeto visa modelar e resolver um problema logístico com base em **estruturas de grafos**, representando vias urbanas como um multigrafo. A proposta é desenvolver uma ferramenta para análise e otimização de rotas de serviços, considerando demandas e restrições de capacidade de veículos.

## 🧠 Definição Formal

O problema é modelado por um **multigrafo conexo G = (V, E, A)**, onde:

- `V`: Conjunto de nós (interseções/esquinas).
- `E`: Conjunto de arestas bidirecionais (vias de mão dupla).
- `A`: Conjunto de arcos direcionados (vias de mão única).

Um subconjunto de nós `VR`, arestas `ER` e arcos `AR` requerem atendimento. A demanda total não pode ultrapassar a capacidade máxima `Q` de cada veículo, e todas as rotas partem e retornam a um nó depósito `v₀`.

---

## 🔨 Etapas do Projeto

### ✅ Etapa 1 — Pré-processamento dos Dados

- Modelagem do problema via estruturas de grafos.
- Leitura de instâncias de entrada.
- Cálculo das seguintes estatísticas:

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

- Geração das **matrizes de caminhos mínimos** e de **predecessores**.

---

## 📋 Requisitos  
- Python 3.12+
- [Jupyter Notebook](https://jupyter.org/)
- Bibliotecas: `pandas`, `jinja2`
---

## 📁 Estrutura do Projeto

```bash
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
 ┃ ┗ 📂utils
 ┃   ┗ 📜utils.py
 ┃ 
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
 ┗ 
📜main.ipynb
📜README.md

```

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/i-am-Gab/trabalho-grafos-2025.git
cd trabalho-grafos-2025
```

### 2. Instale o Python (se ainda não tiver)
Instale o Python 3.12+ a partir do site oficial:
📎 https://www.python.org/downloads/

### 3. Instale as dependencias
```bash
pip install pandas jinja2 notebook
```

## 🔧 Como Usar

### 1. Executando o Notebook
Inicie o Jupyter Notebook
```bash
jupyter notebook
```

### 2. Abra o arquivo main.ipynb pela interface do navegador.
Escolha o arquivo .dat dentro da pasta /storage

Siga as instruções no notebook para rodar cada célula

As métricas e visualizações serão exibidas diretamente no notebook


#### 2.1. Formato do Arquivo de Entrada
O arquivo (ex.: BHW1.dat) deve seguir um formato compatível com instâncias CARP, contendo:

- Nós obrigatórios (ReN.)
  
- Arestas obrigatórias (ReE.)
 
- Arcos obrigatórios (ReA.)

- ARC origem destino 

- Custo travessia 

- Demanda 

- Custo serviço  

- Arestas/arcos não obrigatórios (EDGE/ARC sem demanda)

#### 2.2. Execução

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

---

## Autores

- [@GabrielAguiar](https://https://github.com/i-am-Gab)
- [@ViniciusOliveira](https://github.com/viniciusdev7)
