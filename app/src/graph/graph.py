class Multigraph:
    def __init__(self):
        self.deposito = None
        self.capacidade = None
        self.vertices = set()
        self.arestas = []
        self.arcos = []
        self.nos_obrigatorios = []
        self.arestas_obrigatorias = []
        self.arcos_obrigatorios = []

    def adicionar_no_obrigatorio(self, no, demanda, custo_s):
        self.nos_obrigatorios.append((no, demanda, custo_s))
        self.vertices.add(no)

    def adicionar_aresta_obrigatoria(self, origem, destino, custo_transporte, demanda, custo_s):
        self.arestas_obrigatorias.append((origem, destino, custo_transporte, demanda, custo_s))
        self.vertices.update([origem, destino])

    def adicionar_arco_obrigatorio(self, origem, destino, custo_transporte, demanda, custo_s):
        self.arcos_obrigatorios.append((origem, destino, custo_transporte, demanda, custo_s))
        self.vertices.update([origem, destino])

    def adicionar_aresta(self, origem, destino, custo_transporte):
        self.arestas.append((origem, destino, custo_transporte))
        self.vertices.update([origem, destino])

    def adicionar_arco(self, origem, destino, custo_transporte):
        self.arcos.append((origem, destino, custo_transporte))
        self.vertices.update([origem, destino])
