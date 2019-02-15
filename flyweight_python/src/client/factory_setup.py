from src.factories.operator_factory import OperatorFactory, operator_register
from src.operators.bfs_search_operator import BFSSearchOperator
from src.operators.rename_nodes_operator import RenameNodesOperator


class FactorySetup:

    @staticmethod
    def prepare_factory():
        operator_register(BFSSearchOperator)
        operator_register(RenameNodesOperator)

    @staticmethod
    def get_factory():
        return OperatorFactory
