from src.value_crafter.value_objects.errors.value_object_validation_error import ValueObjectValidationError


class InvalidIdFormatError(ValueObjectValidationError):
    def __init__(self) -> None:
        super().__init__(
            message="User id must be a valid UUID",
        )
