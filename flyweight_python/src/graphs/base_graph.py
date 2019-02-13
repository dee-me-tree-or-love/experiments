class BaseGraph:
    
    def get_edges(self):
        raise NotImplementedError

    def get_nodes(self):
        raise NotImplementedError
    
    def add_edge(self, edge):
        raise NotImplementedError

    def add_node(self, node):
        raise NotImplementedError