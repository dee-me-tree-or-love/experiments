import time

from src.client import FactorySetup, GraphBuilder
from src.errors import UnknownKeyError


def test_operator(operator, test_graph, target):
    start_time = time.time()
    path = operator.search(test_graph, target)
    elapsed_time = time.time() - start_time
    print("----- %.8f ms:" % elapsed_time)
    print(path)
    print("-----\n")
    operator.reset()


def main():
    FactorySetup.prepare_factory()
    factory = FactorySetup.get_factory()
    test_graph = GraphBuilder.build_test_graph()
    test_names = ['Teo', 'Jake', 'Bob', 'Loon', 'Alice', 'Pete', 'Beatrice']

    keys = factory.get_operator_keys()
    operators = list(
        filter(
            lambda o: o is not None,
            map(
                lambda k: factory.get_operator(k), keys
            )
        )
    )

    for o in operators:
        for t in test_names:
            test_operator(o, test_graph, t)


if __name__ == '__main__':
    main()
