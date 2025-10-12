from src.value_crafter.value_objects.errors.value_object_validation_error import ValueObjectValidationError


class RequiredValueError(ValueObjectValidationError):
    def __init__(self) -> None:
        super().__init__(
            message="Value is required, can't be None",
        )
