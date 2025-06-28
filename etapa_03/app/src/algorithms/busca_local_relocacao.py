import copy
from app.src.utils.services import listar_servicos
from app.src.utils.cost import calcular_custo_rota

def busca_local_relocacao(rotas, grafo, distancias, indice, max_iter=10000):
    servicos_info = listar_servicos(grafo)
    servico_por_tupla = {(s['origem'], s['destino']): s for s in servicos_info}

    iteracoes_sem_melhora = 0
    melhorou = True

    while melhorou and iteracoes_sem_melhora < max_iter:
        melhorou = False

        # Relocação entre rotas
        for i in range(len(rotas)):
            for j in range(len(rotas)):
                if i == j:
                    continue

                rota_i = rotas[i]
                rota_j = rotas[j]

                for idx_passo, passo in enumerate(rota_i['rota']):
                    if passo[0] == 'D':
                        continue

                    servico = servico_por_tupla.get((passo[1], passo[2]))
                    if not servico:
                        continue

                    nova_carga_j = rota_j['carga'] + servico['demanda']
                    if nova_carga_j > grafo.capacidade:
                        continue

                    nova_rota_i = copy.deepcopy(rota_i['rota'])
                    nova_rota_i.remove(passo)

                    melhor_custo_j = float('inf')
                    melhor_pos_j = None

                    for pos in range(1, len(rota_j['rota'])):
                        nova_rota_j_temp = copy.deepcopy(rota_j['rota'])
                        nova_rota_j_temp.insert(pos, passo)
                        custo_j = calcular_custo_rota(nova_rota_j_temp, distancias, indice, grafo.deposito, servico_por_tupla)
                        if custo_j < melhor_custo_j:
                            melhor_custo_j = custo_j
                            melhor_pos_j = pos

                    if melhor_pos_j is None:
                        continue

                    nova_rota_j = copy.deepcopy(rota_j['rota'])
                    nova_rota_j.insert(melhor_pos_j, passo)

                    novo_custo_i = calcular_custo_rota(nova_rota_i, distancias, indice, grafo.deposito, servico_por_tupla)
                    custo_atual = rota_i['custo_total'] + rota_j['custo_total']
                    custo_novo = novo_custo_i + melhor_custo_j

                    if custo_novo < custo_atual:
                        rotas[i]['rota'] = nova_rota_i
                        rotas[i]['carga'] -= servico['demanda']
                        rotas[i]['custo_total'] = novo_custo_i

                        rotas[j]['rota'] = nova_rota_j
                        rotas[j]['carga'] += servico['demanda']
                        rotas[j]['custo_total'] = melhor_custo_j

                        melhorou = True

        # Intra-rota 
        for i in range(len(rotas)):
            rota = rotas[i]
            for idx_passo in range(1, len(rota['rota']) - 1):
                passo = rota['rota'][idx_passo]
                if passo[0] == 'D':
                    continue

                melhor_pos = None
                melhor_custo = rota['custo_total']

                for pos in range(1, len(rota['rota']) - 1):
                    if pos == idx_passo:
                        continue

                    nova_rota = copy.deepcopy(rota['rota'])
                    nova_rota.pop(idx_passo)
                    nova_rota.insert(pos, passo)

                    novo_custo = calcular_custo_rota(nova_rota, distancias, indice, grafo.deposito, servico_por_tupla)
                    if novo_custo < melhor_custo:
                        melhor_custo = novo_custo
                        melhor_pos = pos

                if melhor_pos is not None:
                    nova_rota = copy.deepcopy(rota['rota'])
                    nova_rota.pop(idx_passo)
                    nova_rota.insert(melhor_pos, passo)

                    rotas[i]['rota'] = nova_rota
                    rotas[i]['custo_total'] = melhor_custo
                    melhorou = True

        # Swap entre rotas
        for i in range(len(rotas)):
            for j in range(i + 1, len(rotas)):
                rota_i = rotas[i]
                rota_j = rotas[j]

                for idx_passo_i in range(1, len(rota_i['rota']) - 1):
                    passo_i = rota_i['rota'][idx_passo_i]
                    if passo_i[0] == 'D':
                        continue
                    servico_i = servico_por_tupla.get((passo_i[1], passo_i[2]))
                    if not servico_i:
                        continue

                    for idx_passo_j in range(1, len(rota_j['rota']) - 1):
                        passo_j = rota_j['rota'][idx_passo_j]
                        if passo_j[0] == 'D':
                            continue
                        servico_j = servico_por_tupla.get((passo_j[1], passo_j[2]))
                        if not servico_j:
                            continue

                        nova_carga_i = rota_i['carga'] - servico_i['demanda'] + servico_j['demanda']
                        nova_carga_j = rota_j['carga'] - servico_j['demanda'] + servico_i['demanda']

                        if nova_carga_i > grafo.capacidade or nova_carga_j > grafo.capacidade:
                            continue

                        nova_rota_i = copy.deepcopy(rota_i['rota'])
                        nova_rota_j = copy.deepcopy(rota_j['rota'])

                        nova_rota_i[idx_passo_i], nova_rota_j[idx_passo_j] = passo_j, passo_i

                        novo_custo_i = calcular_custo_rota(nova_rota_i, distancias, indice, grafo.deposito, servico_por_tupla)
                        novo_custo_j = calcular_custo_rota(nova_rota_j, distancias, indice, grafo.deposito, servico_por_tupla)

                        custo_atual = rota_i['custo_total'] + rota_j['custo_total']
                        custo_novo = novo_custo_i + novo_custo_j

                        if custo_novo < custo_atual:
                            rotas[i]['rota'] = nova_rota_i
                            rotas[j]['rota'] = nova_rota_j
                            rotas[i]['custo_total'] = novo_custo_i
                            rotas[j]['custo_total'] = novo_custo_j
                            rotas[i]['carga'] = nova_carga_i
                            rotas[j]['carga'] = nova_carga_j
                            melhorou = True

        if melhorou:
            iteracoes_sem_melhora = 0
        else:
            iteracoes_sem_melhora += 1

    return rotas
