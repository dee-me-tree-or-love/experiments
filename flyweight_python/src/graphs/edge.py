from src.graphs.graph_member import GraphMember


class Edge(GraphMember):
    def __init__(self, source, target, label):
        super().__init__()
        self.source = source
        self.target = target
        self.label = label
        self.source.add_edge(self)
        self.target.add_edge(self)

    def __str__(self):
        return "{id: %s, source: %s, target: %s, label: %s}" % (
            self.id,
            str(self.source.name),
            str(self.target.name),
            self.label
        )
