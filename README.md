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

## 📋 Requisitos  
- Python 3.12+  
- Nenhuma dependência externa (usa apenas bibliotecas padrão) 

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

### ✅ Etapa 2 — Solução Inicial

- Desenvolvimento de um algoritmo construtivo para o problema.
- Construção de uma solução que atenda a todas as restrições do problema.
- Garantia das seguintes condições:
  - Não ultrapassar a capacidade dos veículos em cada rota.
  - Cada serviço executado por exatamente uma rota.
  - Caso uma rota passe mais de uma vez por um vértice, aresta ou arco obrigatório, o valor de demanda e o custo de serviço devem ser contabilizados apenas uma vez.
- Testes com todas as instâncias disponibilizadas.
- Organização e entrega das soluções conforme as seguintes orientações:
  - Cada solução é nomeada conforme o padrão:
    - Exemplo: sol-BHW1.dat

---

## 📁 Estrutura do Projeto 

```bash
📂etapa_01
┣  📂app
┃  ┣ 📂src
┃  ┃ ┣ 📂algorithms
┃  ┃ ┃ ┗ 📜algorithms.py
┃  ┃ ┣ 📂graph
┃  ┃ ┃ ┗ 📜graph.py
┃  ┃ ┣ 📂lang
┃  ┃ ┃ ┗ 📜labels.py
┃  ┃ ┣ 📂loader
┃  ┃ ┃ ┗ 📜loader.py
┃  ┃ ┣ 📂metrics
┃  ┃ ┃ ┗ 📜metrics.py
┃  ┃ ┗ 📂utils
┃  ┃   ┗ 📜utils.py
┃  ┗ 📂storage
┃    ┗ 📜Arquivos disponibilizados para teste.
┣ 📜README.md
┗  📜main.ipynb  

📂etapa_02
┣  📂app
┃  ┣ 📂src
┃  ┃ ┣ 📂algorithms
┃  ┃ ┃ ┣ 📜clarke_wright.py
┃  ┃ ┃ ┗ 📜floyd_warshall.py
┃  ┃ ┣ 📂graph
┃  ┃ ┃ ┗ 📜graph.py
┃  ┃ ┣ 📂loader
┃  ┃ ┃ ┗ 📜loader.py
┃  ┃ ┣ 📂metrics
┃  ┃ ┃ ┗ 📜metrics.py
┃  ┃ ┗ 📂utils
┃  ┃   ┣ 📜exporter.py
┃  ┃   ┣ 📜multiple_data.py
┃  ┃   ┣ 📜services_map.py
┃  ┃   ┣ 📜services.py
┃  ┃   ┣ 📜single_data.py
┃  ┃   ┗ 📜utils.py
┃  ┗ 📂storage
┃    ┣ 📂data
┃    ┃   ┣ 📂arquivos
┃    ┃   ┃  ┗📜Arquivos disponibilizados para teste.
┃    ┃   ┗ 📂exemplo_solucoes
┃    ┃      ┗📜Arquivos de solucões exemplo para comparação.
┃    ┣ 📂padroes
┃    ┃   ┗📜Arquivos disponibilizados para padronização do arquivo solução gerado pelo programa.
┃    ┗ 📂solucoes
┃       ┗ 📜Onde ficarão os arquivos das soluções geradas pelo programa.
┣ 📜README.md
┗ 📜main.ipynb 


📜README.md

```

---

Para mais informações, leia o README de cada etapa, disponíveis em:

- [📜 Etapa 01](https://github.com/i-am-Gab/trabalho-grafos-2025/blob/6a216886ac6fea78558d3f33417555a8cec4b85b/etapa_01/README.md)
- [📜 Etapa 02](https://github.com/i-am-Gab/trabalho-grafos-2025/blob/6a216886ac6fea78558d3f33417555a8cec4b85b/etapa_02/README.md)

---

## Autores

- [@GabrielAguiar](https://https://github.com/i-am-Gab)
- [@ViniciusOliveira](https://github.com/viniciusdev7)
