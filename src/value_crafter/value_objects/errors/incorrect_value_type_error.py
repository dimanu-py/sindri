from typing import Any, TypeVar

from src.value_crafter.value_objects.errors.value_object_validation_error import ValueObjectValidationError

T = TypeVar("T")


class IncorrectValueTypeError(ValueObjectValidationError):
    def __init__(self, value: T, expected_type: type[Any]) -> None:
        super().__init__(
            message=f"Value '{value}' is not of type {expected_type.__name__}",
        )
