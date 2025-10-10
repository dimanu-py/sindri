from typing import TypeVar, Any

from src.value_crafter.value_objects.errors.validation_error import ValidationError

T = TypeVar("T")


class IncorrectValueTypeError(ValidationError):
    def __init__(self, value: T, expected_type: type[Any]) -> None:
        super().__init__(
            message=f"Value '{value}' is not of type {expected_type.__name__}",
        )
