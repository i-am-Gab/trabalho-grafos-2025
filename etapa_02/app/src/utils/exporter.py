def salvar_solucao(path_saida, nome_instancia, rotas, custo_total, mapa_servicos, tempo_execucao=0, tempo_solucao=0):
    with open(f"{path_saida}/sol-{nome_instancia}.dat", "w") as f:
        f.write(f"{int(custo_total)}\n")
        f.write(f"{len(rotas)}\n")
        f.write(f"{tempo_execucao}\n")
        f.write(f"{tempo_solucao}\n")

        for i, rota in enumerate(rotas, 1):
            visitas = []

            for passo in rota["rota"]:
                if isinstance(passo, tuple):
                    tipo, u, v = passo
                    sid = mapa_servicos.get((u, v)) or mapa_servicos.get((v, u))
                    if sid:
                        visitas.append(f"(S {sid},{u},{v})")

            total_visitas = len(visitas) + 2
            f.write(f"0 1 {i} {rota['carga']} {int(rota['custo_total'])}  {total_visitas} (D 0,1,1) ")
            f.write(" ".join(visitas))
            f.write(" (D 0,1,1)\n")