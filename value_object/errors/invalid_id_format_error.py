from value_object.errors.validation_error import ValidationError


class InvalidIdFormatError(ValidationError):
    def __init__(self) -> None:
        super().__init__(
            message="User id must be a valid UUID",
        )
