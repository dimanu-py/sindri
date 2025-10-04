from src.errors.validation_error import ValidationError


class RequiredValueError(ValidationError):
    def __init__(self) -> None:
        super().__init__(
            message="Value is required, can't be None",
        )
