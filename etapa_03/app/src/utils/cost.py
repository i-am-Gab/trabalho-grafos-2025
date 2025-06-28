def calcular_custo_rota(rota, distancias, indice, deposito, servico_por_tupla):
    custo = 0
    anterior = deposito
    for passo in rota:
        if passo[0] == 'D':
            continue
        atual = passo[1]
        custo += distancias[indice[anterior]][indice[atual]]

        # Adiciona o custo de serviço
        servico = servico_por_tupla.get((passo[1], passo[2]))
        if servico:
            custo += servico['custo_s']

        anterior = passo[2]
    custo += distancias[indice[anterior]][indice[deposito]]
    return custo
