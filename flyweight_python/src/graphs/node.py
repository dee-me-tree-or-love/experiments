from src.graphs.graph_member import GraphMember


class Node(GraphMember):
    def __init__(self, label, name):
        super().__init__()
        self.label = label
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return "{id: %s, label: %s, name: %s, edges: %s}" % (
            self.id,
            self.label,
            self.name,
            list(map(lambda e: str(e), self.edges))
        )
