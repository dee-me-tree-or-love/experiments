from src.graphs import ListBasedGraph, Edge, Node


class GraphBuilder:

    @staticmethod
    def build_test_graph():
        node_label = "Person"
        edge_label = "Knows"
        names = ['Pete', 'Alice', 'Jake', 'Beatrice', 'Pluto', 'Teo']

        nodes = list(map(lambda n: Node(node_label, n), names))
        edges = [
            Edge(nodes[0], nodes[1], edge_label),
            Edge(nodes[0], nodes[2], edge_label),
            Edge(nodes[2], nodes[3], edge_label),
            Edge(nodes[1], nodes[4], edge_label),
            Edge(nodes[4], nodes[5], edge_label),
            Edge(nodes[3], nodes[5], edge_label)
        ]

        graph = ListBasedGraph(nodes=nodes, edges=edges)
        return graph
