from app.src.utils.services import listar_servicos

def clarke_wright(grafo, distancias, indice):
    deposito = grafo.deposito
    capacidade = grafo.capacidade
    servicos = listar_servicos(grafo)
    rotas = []
    servico_para_rota = {}

    # Criar rota inicial para cada serviço
    for idx, s in enumerate(servicos):
        custo_inicio = distancias[indice[deposito]][indice[s['origem']]]
        custo_fim = distancias[indice[s['destino']]][indice[deposito]]
        custo_total = custo_inicio + s['custo_s'] + custo_fim

        rota = {
            'servicos': [s],
            'carga': s['demanda'],
            'custo_total': custo_total,
            'inicio': s['origem'],
            'fim': s['destino']
        }

        rotas.append(rota)
        servico_para_rota[idx] = rota

    # Calcular savings para todos os pares de serviços
    savings = []
    for i in range(len(servicos)):
        for j in range(len(servicos)):
            if i == j:
                continue
            si = servicos[i]
            sj = servicos[j]
            saving = (
                distancias[indice[si['destino']]][indice[deposito]] +
                distancias[indice[deposito]][indice[sj['origem']]] -
                distancias[indice[si['destino']]][indice[sj['origem']]]
            )
            savings.append((saving, i, j))

    # Ordenar savings do maior para o menor
    savings.sort(reverse=True)

    # Tentar unir rotas com base nos savings
    for saving, i, j in savings:
        rota_i = servico_para_rota.get(i)
        rota_j = servico_para_rota.get(j)

        if rota_i is None or rota_j is None or rota_i == rota_j:
            continue

        if rota_i['fim'] == servicos[i]['destino'] and rota_j['inicio'] == servicos[j]['origem']:
            nova_carga = rota_i['carga'] + rota_j['carga']
            if nova_carga <= capacidade:
                nova_servicos = rota_i['servicos'] + rota_j['servicos']

                novo_custo = (
                    distancias[indice[deposito]][indice[rota_i['inicio']]] +
                    sum(s['custo_s'] for s in nova_servicos) +
                    distancias[indice[rota_i['fim']]][indice[rota_j['inicio']]] +
                    distancias[indice[rota_j['fim']]][indice[deposito]]
                )

                nova_rota = {
                    'servicos': nova_servicos,
                    'carga': nova_carga,
                    'custo_total': novo_custo,
                    'inicio': rota_i['inicio'],
                    'fim': rota_j['fim']
                }

                if rota_i in rotas and rota_j in rotas:
                    rotas.remove(rota_i)
                    rotas.remove(rota_j)
                    rotas.append(nova_rota)

                    # Atualiza o mapeamento para todos os serviços da nova rota
                    for idx_s, servico in enumerate(servicos):
                        if servico in nova_servicos:
                            servico_para_rota[idx_s] = nova_rota
    
    # Converter rotas para formato final de saída
    resultado = []
    # Converter rotas para formato final de saída
    resultado = []
    for rota in rotas:
        passos = []
        passos.append(('D', deposito, deposito))  # Início no depósito
        passos.extend((s['tipo'], s['origem'], s['destino']) for s in rota['servicos'])
        passos.append(('D', deposito, deposito))  # Fim no depósito

        resultado.append({
            'rota': passos,
            'custo_total': rota['custo_total'],
            'carga': rota['carga']
        })


    return resultado