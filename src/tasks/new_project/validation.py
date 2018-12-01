from src.tasks.new_project.errors import InputError


class Validator:
    """
    Encapsulates the validation logic
    """

    @classmethod
    def validate_project_name(cls, project_name):
        if not project_name:
            cls.__raise_validation_error()


    @classmethod
    def __raise_validation_error(cls):
        raise InputError(
            "supplied project name is not valid: %s" % project_name
        )