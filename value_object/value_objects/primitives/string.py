from value_object.errors.incorrect_value_type_error import IncorrectValueTypeError
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.decorators.validation import validate
from value_object.value_objects.value_object import ValueObject


class String(ValueObject[str]):
    """
    A value object that wraps string values with validation.

    This class provides a base implementation for creating value objects that
    represent string values in the domain. It ensures that the wrapped value
    is a valid string and not None.

    The class includes built-in validation for:
    - Required value (not None)
    - Type checking (must be a string)

    Inherits all functionality from ValueObject including immutability,
    equality comparison, string representation, and hashing.

    Example:
        >>> class Email(String):
        ...     @validate
        ...     def _validate_email_format(self, value: str) -> None:
        ...         if "@" not in value:
        ...             raise ValueError("Invalid email format")
        ...
        >>> email = Email("user@example.com")
        >>> email.value
        'user@example.com'
    """

    @validate
    def _ensure_has_value(self, value: str) -> None:
        """
        Validate that the provided value is not None.

        This validator ensures that required string values are provided
        and prevents None values from being stored in the value object.

        Args:
            value: The string value to validate.

        Raises:
            RequiredValueError: If the value is None.

        Example:
            >>> String("hello")  # Valid
            StringValueObject('hello')
            >>> String("")  # Valid empty string
            StringValueObject('')
            >>> # StringValueObject(None)  # Would raise RequiredValueError
        """
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_is_string(self, value: str) -> None:
        """
        Validate that the provided value is of string type.

        This validator ensures type safety by checking that the value
        is actually a string. This prevents other types like integers,
        floats, or other objects from being accepted.

        Args:
            value: The value to validate for string type.

        Raises:
            IncorrectValueTypeError: If the value is not a string.

        Example:
            >>> String("hello")  # Valid string
            StringValueObject('hello')
            >>> # StringValueObject(123)  # Would raise IncorrectValueTypeError
            >>> # StringValueObject(['a', 'b'])  # Would raise IncorrectValueTypeError
        """
        if not isinstance(value, str):
            raise IncorrectValueTypeError(value)
