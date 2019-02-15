from src.operators.base_operator import BaseOperator


class RenameNodesOperator(BaseOperator):
    _KEY = 'rename_nodes'

    def perform(self, graph, start_name, end_name):
        nodes = graph.get_nodes()
        for n in nodes:
            n.name = end_name if n.name == start_name else n.name
