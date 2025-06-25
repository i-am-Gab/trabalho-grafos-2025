## 📁 Estrutura do Projeto 2

```bash
📂etapa_03
┣  📂app
┃  ┣ 📂src
┃  ┃ ┣ 📂algorithms
┃  ┃ ┃ ┣ 📜busca_local_relocacao.py
┃  ┃ ┃ ┣ 📜clarke_wright.py
┃  ┃ ┃ ┗ 📜floyd_warshall.py
┃  ┃ ┣ 📂graph
┃  ┃ ┃ ┗ 📜graph.py
┃  ┃ ┣ 📂loader
┃  ┃ ┃ ┗ 📜loader.py
┃  ┃ ┣ 📂metrics
┃  ┃ ┃ ┗ 📜metrics.py
┃  ┃ ┗ 📂utils
┃  ┃   ┣ 📜exporter.py
┃  ┃   ┣ 📜multiple_data.py
┃  ┃   ┣ 📜services_map.py
┃  ┃   ┣ 📜services.py
┃  ┃   ┣ 📜single_data.py
┃  ┃   ┗ 📜utils.py
┃  ┗ 📂storage
┃    ┣ 📂data
┃    ┃   ┣ 📂arquivos
┃    ┃   ┃  ┗📜Arquivos disponibilizados para teste.
┃    ┃   ┗ 📂exemplo_solucoes
┃    ┃      ┗📜Arquivos de solucões exemplo para comparação.
┃    ┣ 📂padroes
┃    ┃   ┗📜Arquivos disponibilizados para padronização do arquivo solução gerado pelo programa.
┃    ┗ 📂solucoes
┃       ┗ 📜Onde ficarão os arquivos das soluções geradas pelo programa.
┣ 📜README.md
┗ 📜main.ipynb 


📜README.md

```

---


## 🔧 Como Usar

### 1. Formato do Arquivo de Entrada
O arquivo (ex.: BHW1.dat) deve seguir um formato compatível com instâncias CARP, contendo:

- Nós obrigatórios (ReN.)
  
- Arestas obrigatórias (ReE.)
 
- Arcos obrigatórios (ReA.)

- ARC origem destino 

- Custo travessia 

- Demanda 

- Custo serviço  

- Arestas/arcos não obrigatórios (EDGE/ARC sem demanda)

### 2. Execução

Execute o arquivo main.ipynb localizado dentro de 📂etapa_03

Informe a maneira com que você deseja executar o programa:
    1 - Executar arquivo único.
    2 - Executar para todos os arquivos na pasta 📂storage/data/arquivos.

Caso opte pela opção 1:
- Insira o nome do arquivo .dat que será lido pelo programa.
  - O arquivo deve estar dentro de 📂storage/data/arquivos;
  - O arquivo deve estar formatado de acordo com os demais arquivos presentes na pasta.
  - O arquivo solução será gerado dentro de 📂storage/solucoes. E o nome seguirá o padrão "sol-'nome do arquivo escolhido'.dat".
  - Será retornada uma mensagem indicando sucesso ou falha na execução.

Caso opte pela opção 2:
- Basta esperar que o programa automaticamente irá reconhecer todos os arquivos na pasta e irá executar os algoritmos para cada um.
    - O arquivo solução será gerado dentro de 📂storage/solucoes. E o nome seguirá o padrão "sol-'nome do arquivo escolhido'.dat".
    - Será retornada uma mensagem indicando sucesso ou falha na execução.
