from value_object.errors.validation_error import ValidationError


class InvalidNegativeValueError(ValidationError):
    def __init__(self, value: int) -> None:
        super().__init__(
            message=f"Invalid negative value: {value}",
        )
