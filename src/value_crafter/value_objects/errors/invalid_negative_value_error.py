from src.value_crafter.value_objects.errors.value_object_validation_error import ValueObjectValidationError


class InvalidNegativeValueError(ValueObjectValidationError):
    def __init__(self, value: int) -> None:
        super().__init__(
            message=f"Invalid negative value: {value}",
        )
