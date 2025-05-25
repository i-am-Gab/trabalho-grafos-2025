import time
import os

from app.src.loader.loader import carregar_instancia
from app.src.algorithms.floyd_warshall import floyd_warshall
from app.src.algorithms.path_scanning import path_scanning
from app.src.utils.service_map import mapear_servicos_para_id_servico
from app.src.utils.exporter import salvar_solucao

def executar_algoritmo_arquivos_multiplos(resultado, caminho_saida, CLOCKS_PER_SEC):
    for caminho in resultado:
        inicio_execucao = time.perf_counter()
        
        nome_instancia = os.path.splitext(os.path.basename(caminho))[0]
        
        grafo = carregar_instancia(caminho)
        distancias, predecessores, index = floyd_warshall(grafo)

        inicio_solucao = time.perf_counter()
        rotas = path_scanning(grafo, distancias, index)
        fim_solucao = time.perf_counter()
        
        mapa_servicos = mapear_servicos_para_id_servico(grafo)
        custo_total = sum(rota["custo_total"] for rota in rotas)
        
        fim_execucao = time.perf_counter()
        
        tempo_solucao = int((fim_solucao - inicio_solucao) * CLOCKS_PER_SEC)
        tempo_execucao = int((fim_execucao - inicio_execucao) * CLOCKS_PER_SEC)
        
        salvar_solucao(
            path_saida=caminho_saida,
            nome_instancia=nome_instancia,
            rotas=rotas,
            custo_total=custo_total,
            mapa_servicos=mapa_servicos,
            tempo_execucao=tempo_execucao,
            tempo_solucao=tempo_solucao
        )