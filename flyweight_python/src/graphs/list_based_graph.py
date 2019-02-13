from src.graphs.base_graph import BaseGraph


class ListBasedGraph(BaseGraph):

    def __init__(self, nodes=[], edges=[]):
        self._nodes = nodes
        self._edges = edges

    def get_edges(self):
        return list(self._edges)

    def get_nodes(self):
        return list(self._nodes)

    def add_edge(self, edge):
        self._edges.append(edge)

    def add_node(self, node):
        self._nodes.append(node)
