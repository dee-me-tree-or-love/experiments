from src.errors.unknown_key_error import UnknownKeyError


class OperatorFactory:
    """
    """

    _operators = {}

    @classmethod
    def register_operator(cls, key, registering_operator):
        cls._operators[key] = registering_operator

    @classmethod
    def get_operator(cls, key):
        try:
            return cls._operators[key].create()
        except KeyError:
            return None
            # raise UnknownKeyError(key)

    @classmethod
    def get_operator_keys(cls):
        return list(cls._operators.keys())


class operator_register(object):

    def __init__(self, operator_class):
        print("registering: %s" % operator_class.get_key())

        OperatorFactory.register_operator(
            operator_class.get_key(),
            operator_class
        )

        print(OperatorFactory.get_operator_keys())
