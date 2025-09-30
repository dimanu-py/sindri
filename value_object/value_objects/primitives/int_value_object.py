from value_object.errors.incorrect_value_type_error import IncorrectValueTypeError
from value_object.errors.invalid_negative_value_error import InvalidNegativeValueError
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.decorators.validation import validate
from value_object.value_objects.value_object import ValueObject


class IntValueObject(ValueObject[int]):
    @validate
    def _ensure_has_value(self, value: int) -> None:
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_integer(self, value: int) -> None:
        if not isinstance(value, int):
            raise IncorrectValueTypeError(value)

    @validate
    def _ensure_value_is_positive(self, value: int) -> None:
        if value < 0:
            raise InvalidNegativeValueError(value)
