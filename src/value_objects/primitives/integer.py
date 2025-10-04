from src.errors.incorrect_value_type_error import IncorrectValueTypeError
from src.errors.required_value_error import RequiredValueError
from src.value_objects.decorators.validation import validate
from src.value_objects.value_object import ValueObject


class Integer(ValueObject[int]):
    """
    A value object that wraps integer values with validation.

    This class provides a base implementation for creating value objects that
    represent integer values in the domain. It ensures that the wrapped value
    is a valid integer and not None.

    The class includes built-in validation for:
    - Required value (not None)
    - Type checking (must be an integer)

    Inherits all functionality from ValueObject including immutability,
    equality comparison, string representation, and hashing.

    Example:
        >>> class Age(Integer):
        ...     @validate
        ...     def _validate_positive(self, value: int) -> None:
        ...         if value < 0:
        ...             raise ValueError("Age cannot be negative")
        ...
        >>> age = Age(25)
        >>> age.value
        25
        >>> str(age)
        '25'
    """

    @validate
    def _ensure_has_value(self, value: int) -> None:
        """
        Validate that the provided value is not None.

        This validator ensures that required integer values are provided
        and prevents None values from being stored in the value object.

        Args:
            value: The integer value to validate.

        Raises:
            RequiredValueError: If the value is None.

        Example:
            >>> Integer(42)  # Valid
            IntValueObject(42)
            >>> Integer(None)  # Raises RequiredValueError
            Traceback (most recent call last):
                ...
            RequiredValueError: ...
        """
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_integer(self, value: int) -> None:
        """
        Validate that the provided value is of integer type.

        This validator ensures type safety by checking that the value
        is actually an integer. This prevents other numeric types like
        float or string representations of numbers from being accepted.

        Args:
            value: The value to validate for integer type.

        Raises:
            IncorrectValueTypeError: If the value is not an integer.

        Example:
            >>> Integer(42)  # Valid integer
            IntValueObject(42)
            >>> Integer(42.0)  # Raises IncorrectValueTypeError
            Traceback (most recent call last):
                ...
            IncorrectValueTypeError: ...
            >>> Integer("42")  # Raises IncorrectValueTypeError
            Traceback (most recent call last):
                ...
            IncorrectValueTypeError: ...
        """
        if not isinstance(value, int):
            raise IncorrectValueTypeError(value)
