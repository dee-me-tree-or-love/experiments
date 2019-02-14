from src.factories.operator_factory import OperatorFactory, operator_register
from src.operators.bfs_search_operator import BFSSearchOperator


class FactorySetup:

    @staticmethod
    def prepare_factory():
        operator_register(BFSSearchOperator)

    @staticmethod
    def get_factory():
        return OperatorFactory
