from src.operators.path import Path


class BaseOperator:
    _KEY = "base"

    def search(self, graph, target):
        raise NotImplementedError("Perform must be operator specific")

    def reset(self):
        self.__init__()

    @classmethod
    def get_key(cls):
        return cls._KEY

    @classmethod
    def create(cls):
        return cls()
