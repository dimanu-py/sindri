from typing import TypeVar

from src.value_crafter.value_objects.errors.validation_error import ValidationError

T = TypeVar("T")


class IncorrectValueTypeError(ValidationError):
    def __init__(self, value: T) -> None:
        super().__init__(
            message=f"Value '{value}' is not of type {type(value).__name__}",
        )
