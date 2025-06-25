import copy
from app.src.utils.services import listar_servicos

def calcular_custo_rota(rota, distancias, indice, deposito):
    custo = 0
    anterior = deposito
    for passo in rota:
        if passo[0] == 'D':
            continue
        atual = passo[1]
        custo += distancias[indice[anterior]][indice[atual]]
        anterior = passo[2]
        # Custo de serviço será somado fora, se necessário
    custo += distancias[indice[anterior]][indice[deposito]]
    return custo

def busca_local_relocacao(rotas, grafo, distancias, indice):
    servicos_info = listar_servicos(grafo)
    servico_por_tupla = {(s['origem'], s['destino']): s for s in servicos_info}

    melhorou = True
    while melhorou:
        melhorou = False
        for i in range(len(rotas)):
            for j in range(len(rotas)):
                if i == j:
                    continue

                rota_i = rotas[i]
                rota_j = rotas[j]

                for idx_passo, passo in enumerate(rota_i['rota']):
                    if passo[0] == 'D':
                        continue  # Ignora o depósito

                    # Tenta mover o serviço passo de i -> j
                    novo_servico = servico_por_tupla.get((passo[1], passo[2]))
                    if not novo_servico:
                        continue

                    nova_carga_j = rota_j['carga'] + novo_servico['demanda']
                    if nova_carga_j > grafo.capacidade:
                        continue

                    nova_rota_i = copy.deepcopy(rota_i['rota'])
                    nova_rota_j = copy.deepcopy(rota_j['rota'])

                    nova_rota_i.remove(passo)
                    nova_rota_j.insert(-1, passo)  # Antes do último depósito

                    novo_custo_i = calcular_custo_rota(nova_rota_i, distancias, indice, grafo.deposito)
                    novo_custo_j = calcular_custo_rota(nova_rota_j, distancias, indice, grafo.deposito)

                    custo_atual = rota_i['custo_total'] + rota_j['custo_total']
                    custo_novo = novo_custo_i + novo_custo_j

                    if custo_novo < custo_atual:
                        rotas[i]['rota'] = nova_rota_i
                        rotas[i]['carga'] -= novo_servico['demanda']
                        rotas[i]['custo_total'] = novo_custo_i

                        rotas[j]['rota'] = nova_rota_j
                        rotas[j]['carga'] += novo_servico['demanda']
                        rotas[j]['custo_total'] = novo_custo_j

    return rotas
