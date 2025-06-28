import time
import os

from app.src.loader.loader import carregar_instancia
from app.src.algorithms.floyd_warshall import floyd_warshall
from app.src.algorithms.clarke_wright import clarke_wright
from app.src.utils.service_map import mapear_servicos_para_id_servico
from app.src.utils.exporter import salvar_solucao
from app.src.algorithms.busca_local_relocacao import busca_local_relocacao
from app.src.algorithms.busca_local_relocacao import calcular_custo_rota
from app.src.utils.services import listar_servicos

def executar_algoritmo_arquivos_multiplos(resultado, caminho_saida):
    for caminho in resultado:
        inicio_execucao = time.perf_counter()
        
        nome_instancia = os.path.splitext(os.path.basename(caminho))[0]
        
        grafo = carregar_instancia(caminho)
        distancias, predecessores, index = floyd_warshall(grafo)

        inicio_solucao = time.perf_counter()
        rotas = clarke_wright(grafo, distancias, index)
        rotas = busca_local_relocacao(rotas, grafo, distancias, index)
        fim_solucao = time.perf_counter()
        
        mapa_servicos = mapear_servicos_para_id_servico(grafo)

        for rota in rotas:
            servicos_info = listar_servicos(grafo)
            servico_por_tupla = {(s['origem'], s['destino']): s for s in servicos_info}
            novo_custo = calcular_custo_rota(rota['rota'], distancias, index, grafo.deposito, servico_por_tupla)
            rota['custo_total'] = novo_custo

        custo_total = sum(rota["custo_total"] for rota in rotas)
        
        fim_execucao = time.perf_counter()
        
        tempo_solucao = int((fim_solucao - inicio_solucao) * 1_000_000)
        tempo_execucao = int((fim_execucao - inicio_execucao) * 1_000_000)
        
        salvar_solucao(
            path_saida=caminho_saida,
            nome_instancia=nome_instancia,
            rotas=rotas,
            custo_total=custo_total,
            mapa_servicos=mapa_servicos,
            deposito=grafo.deposito,
            tempo_execucao=tempo_execucao,
            tempo_solucao=tempo_solucao
        )

    print("Os arquivos solução foram salvos com sucesso! Os mesmos podem ser encontrados em:")
    print(f"etapa_03/{caminho_saida}")