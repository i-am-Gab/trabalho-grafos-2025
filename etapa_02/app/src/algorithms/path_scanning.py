from app.src.utils.services import listar_servicos

def path_scanning(grafo, distancias, indice):
    servicos = listar_servicos(grafo)
    restantes = list(servicos)
    rotas = []

    deposito = grafo.deposito
    capacidade = grafo.capacidade

    while restantes:
        rota = [deposito]
        carga = 0
        custo = 0
        atual = deposito
        passos = []

        while True:
            candidatos = []
            for s in restantes:
                if s['demanda'] + carga <= capacidade:
                    candidatos.append(s)

            if not candidatos:
                break

            menor = None
            menor_dist = float('inf')
            for s in candidatos:
                d = distancias[indice[atual]][indice[s['origem']]]
                if d < menor_dist:
                    menor = s
                    menor_dist = d

            passos.append((menor['tipo'], menor['origem'], menor['destino']))
            custo += menor_dist + menor['custo_s']
            carga += menor['demanda']
            atual = menor['destino']
            restantes.remove(menor)

        custo += distancias[indice[atual]][indice[deposito]]
        passos.append(deposito)
        rotas.append({
            "rota": passos,
            "custo_total": custo,
            "carga": carga
        })

    return rotas