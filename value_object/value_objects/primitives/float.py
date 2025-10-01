from value_object.errors.incorrect_value_type_error import IncorrectValueTypeError
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.decorators.validation import validate
from value_object.value_objects.value_object import ValueObject


class Float(ValueObject[float]):
    """
    A value object that wraps float values with validation.

    This class provides a base implementation for creating value objects that
    represent float values in the domain. It ensures that the wrapped value
    is a valid float and not None. It accepts both positive and negative values.

    The class includes built-in validation for:
    - Required value (not None)
    - Type checking (must be a float)

    Inherits all functionality from ValueObject including immutability,
    equality comparison, string representation, and hashing.

    Example:
        >>> class Price(Float):
        ...     @validate
        ...     def _validate_positive(self, value: float) -> None:
        ...         if value < 0:
        ...             raise ValueError("Price cannot be negative")
        ...
        >>> price = Price(29.99)
        >>> price.value
        29.99
        >>> str(price)
        '29.99'
    """

    @validate
    def _ensure_has_value(self, value: float) -> None:
        """
        Validate that the provided value is not None.

        This validator ensures that required float values are provided
        and prevents None values from being stored in the value object.

        Args:
            value: The float value to validate.

        Raises:
            RequiredValueError: If the value is None.

        Example:
            >>> Float(3.14)  # Valid
            FloatValueObject(3.14)
            >>> Float(-2.5)  # Valid negative
            FloatValueObject(-2.5)
            >>> # FloatValueObject(None)  # Would raise RequiredValueError
        """
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_float(self, value: float) -> None:
        """
        Validate that the provided value is of float type.

        This validator ensures type safety by checking that the value
        is actually a float. This prevents other numeric types like
        integers or string representations of numbers from being accepted.

        Args:
            value: The value to validate for float type.

        Raises:
            IncorrectValueTypeError: If the value is not a float.

        Example:
            >>> Float(3.14)  # Valid float
            FloatValueObject(3.14)
            >>> # FloatValueObject(42)  # Would raise IncorrectValueTypeError (integer)
            >>> # FloatValueObject("3.14")  # Would raise IncorrectValueTypeError (string)
        """
        if not isinstance(value, float):
            raise IncorrectValueTypeError(value)
