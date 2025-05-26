def escolher_arquivos(diretorio):
    import os
    arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    ultima_opcao = None

    while True:
        print("\nEscolha uma opção:")
        print("1 - Ler um arquivo específico")
        print("2 - Executar para todos os arquivos")
        print("0 - Sair")

        if ultima_opcao not in [None, '0']:
            print(f"Última opção '{ultima_opcao}' foi inválida.")

        opcao = input("Digite 1, 2 ou 0: ").strip()

        if opcao == '1':
            nome_arquivo = input("Digite o nome do arquivo: ").strip() + '.dat'
            if nome_arquivo in arquivos:
                caminho = os.path.join(diretorio, nome_arquivo)
                return caminho 
            else:
                print("Arquivo não encontrado no diretório.")

        elif opcao == '2':
            caminhos = [os.path.join(diretorio, nome) for nome in arquivos]
            return caminhos

        elif opcao == '0':
            print("Saindo...")
            return None

        else:
            print("Opção inválida.")
            ultima_opcao = opcao