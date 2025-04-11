import pandas as pd
import jinja2
import math
from app.src.lang.labels import metric_labels

def imprimir_matriz_dist(distancias, indice):
    vertices = sorted(indice.keys())
    num_vertices = len(vertices)

    matriz_dist = []
    for i in range(num_vertices):
        linha = []
        for j in range(num_vertices):
            if distancias[i][j] != float('inf'):
                linha.append(round(distancias[i][j], 1))
            else:
                linha.append(math.inf)
        matriz_dist.append(linha)

    df_dist = pd.DataFrame(matriz_dist, index=vertices, columns=vertices)
    df_dist.index.name = "Origem"
    df_dist.columns.name = "Destino"
    df_dist = df_dist.style.set_properties(**{'text-align': 'center'})
    return df_dist

def imprimir_matriz_pred(predecessores, indice):
    vertices = sorted(indice.keys())
    num_vertices = len(vertices)
    
    matriz_pred = []
    for i in range(num_vertices):
        linha = []
        for j in range(num_vertices):
            if predecessores[i][j] is not None:
                linha.append(vertices[predecessores[i][j]])
            else:
                linha.append("-" if i == j else None)
        matriz_pred.append(linha)

    df_pred = pd.DataFrame(matriz_pred, index=vertices, columns=vertices)
    df_pred.index.name = "Origem"
    df_pred.columns.name = "Destino"
    df_pred = df_pred.style.set_properties(**{'text-align': 'center'})
    return df_pred
    
def imprimir_dados_grafo(dados_metricas):
    metricas_grafo = {
        "Métricas": [
            metric_labels["tipo"],
            metric_labels["num_vertices"],
            metric_labels["num_arestas"],
            metric_labels["num_arcos"],
            metric_labels["num_nos_obrigatorios"],
            metric_labels["num_arestas_obrigatorias"],
            metric_labels["num_arcos_obrigatorios"],
            metric_labels["densidade"],
            metric_labels["grau_minimo"],
            metric_labels["grau_maximo"],
            metric_labels["caminho_medio"],
            metric_labels["diametro"]
        ],
        "Valor": [
            metric_labels[dados_metricas["tipo"]],
            dados_metricas["num_vertices"],
            dados_metricas["num_arestas"],
            dados_metricas["num_arcos"],
            dados_metricas["num_nos_obrigatorios"],
            dados_metricas["num_arestas_obrigatorias"],
            dados_metricas["num_arcos_obrigatorios"],
            dados_metricas["densidade"],
            dados_metricas["grau_minimo"],
            dados_metricas["grau_maximo"],
            dados_metricas["caminho_medio"],
            dados_metricas["diametro"]
        ]
    }

    df_itens = pd.DataFrame(metricas_grafo)
    df_itens.index = range(1, len(df_itens) + 1)
    df_itens.columns.name = "ID"
    df_itens = df_itens.style.set_properties(**{'text-align': 'left'})
    return df_itens

def imprimir_intermediacao(intermediacao):
    dados_intermediacao = {
        "Vértices": list(intermediacao.keys()),
        "Intermediação": list(intermediacao.values())
    }

    df_intermediacao = pd.DataFrame(dados_intermediacao)
    df_intermediacao.index = range(1, len(df_intermediacao) + 1)
    df_intermediacao.columns.name = "ID"
    df_intermediacao = df_intermediacao.style.set_properties(**{'text-align': 'center'})
    return df_intermediacao