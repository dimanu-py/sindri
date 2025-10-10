from src.value_crafter.value_objects.errors.validation_error import ValidationError


class InvalidNegativeValueError(ValidationError):
    def __init__(self, value: int) -> None:
        super().__init__(
            message=f"Invalid negative value: {value}",
        )
