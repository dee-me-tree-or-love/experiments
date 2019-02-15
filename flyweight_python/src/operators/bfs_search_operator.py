from collections import deque

from src.operators.base_operator import BaseOperator, Path


class BFSSearchOperator(BaseOperator):
    _KEY = "bfs_search"

    def __init__(self):
        self._open_set = deque()
        self._closed_set = set()
        self._path = []

    def perform(self, graph, start_name, end_name):
        return self.search(graph, start_name, end_name)

    def search(self, graph, start_name, target_name):
        """
        """
        nodes = list(graph.get_nodes())
        print(list(map(lambda n: str(n), nodes)))
        possible_starts = (list(filter(lambda n: n.name == start_name, nodes)))
        if len(possible_starts) > 0: 
            start = possible_starts.pop()
            print(start)
            print("~~")
            self._add_to_queue(start)

        path = self._lookup_target(target_name)
        return path

    def _lookup_target(self, goal_name):
        print(self._open_set)
        if len(self._open_set) == 0:
            return Path(target=goal_name)

        node = self._open_set.pop()
        self._add_to_path(node)

        if self._check_predicate(node, goal_name):
            return Path(self._path, self._path[0], node)

        for e in node.edges:
            print(e.source.name)
            print(e.target.name)
            self._add_to_queue(e.target)
            self._add_to_queue(e.source)
            self._close_step(node)

        return self._lookup_target(goal_name)

    def _check_predicate(self, node, goal_name):
        return node.name == goal_name

    def _add_to_queue(self, node):
        print(node.name)
        if not node in self._closed_set:
            self._open_set.append(node)

    def _close_step(self, node):
        self._closed_set.add(node)

    def _add_to_path(self, node):
        self._path.append(node)