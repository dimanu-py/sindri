from src.errors.incorrect_value_type_error import IncorrectValueTypeError
from src.errors.required_value_error import RequiredValueError
from src.value_objects.decorators.validation import validate
from src.value_objects.value_object import ValueObject


class Boolean(ValueObject[bool]):
    """
    A value object that wraps boolean values with validation.

    This class provides a base implementation for creating value objects that
    represent boolean values in the domain. It ensures that the wrapped value
    is a valid boolean and not None.

    The class includes built-in validation for:
    - Required value (not None)
    - Type checking (must be a boolean)

    Inherits all functionality from ValueObject including immutability,
    equality comparison, string representation, and hashing.

    Example:
        >>> class IsActive(Boolean):
        ...     @validate
        ...     def _validate_true_for_premium(self, value: bool) -> None:
        ...         # Custom business logic can be added here
        ...         pass
        ...
        >>> is_active = IsActive(True)
        >>> is_active.value
        True
        >>> str(is_active)
        'True'
    """

    @validate
    def _ensure_has_value(self, value: bool) -> None:
        """
        Validate that the provided value is not None.

        This validator ensures that required boolean values are provided
        and prevents None values from being stored in the value object.

        Args:
            value: The boolean value to validate.

        Raises:
            RequiredValueError: If the value is None.

        Example:
            >>> Boolean(True)  # Valid
            BooleanValueObject(True)
            >>> Boolean(False)  # Valid
            BooleanValueObject(False)
            >>> # BooleanValueObject(None)  # Would raise RequiredValueError
        """
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_boolean(self, value: bool) -> None:
        """
        Validate that the provided value is of boolean type.

        This validator ensures type safety by checking that the value
        is actually a boolean. This prevents other types like integers
        (0, 1) or string representations ("true", "false") from being accepted.

        Args:
            value: The value to validate for boolean type.

        Raises:
            IncorrectValueTypeError: If the value is not a boolean.

        Example:
            >>> Boolean(True)  # Valid boolean
            BooleanValueObject(True)
            >>> Boolean(False)  # Valid boolean
            BooleanValueObject(False)
            >>> # BooleanValueObject(1)  # Would raise IncorrectValueTypeError (integer)
            >>> # BooleanValueObject("true")  # Would raise IncorrectValueTypeError (string)
            >>> # BooleanValueObject(0)  # Would raise IncorrectValueTypeError (integer)
        """
        if not isinstance(value, bool):
            raise IncorrectValueTypeError(value)
