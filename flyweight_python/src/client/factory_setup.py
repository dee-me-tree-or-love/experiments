from src.factories.operator_factory import OperatorFactory, operator_register
from src.operators.bfs_operator import BFSOperator


class FactorySetup:

    @staticmethod
    def prepare_factory():
        operator_register(BFSOperator)

    @staticmethod
    def get_factory():
        return OperatorFactory
