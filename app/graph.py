class Multigraph:
    def __init__(self):
        self.depot = None
        self.capacity = None
        self.vertices = set()
        self.edges = []
        self.arcs = []
        self.required_nodes = []
        self.required_edges = []
        self.required_arcs = []