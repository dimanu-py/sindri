from uuid import UUID

from value_object.errors.incorrect_value_type_error import IncorrectValueTypeError
from value_object.errors.invalid_id_format_error import InvalidIdFormatError
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.decorators.validation import validate
from value_object.value_objects.value_object import ValueObject


class Uuid(ValueObject[str]):
    """
    A value object that wraps UUID (Universally Unique Identifier) string values with validation.

    This class provides a specialized implementation for creating value objects that
    represent UUID values in the domain. It ensures that the wrapped value is a
    valid UUID string format and not None.

    The class includes built-in validation for:
    - Required value (not None)
    - Type checking (must be a string)
    - UUID format validation (must be a valid UUID format)

    Inherits all functionality from ValueObject including immutability,
    equality comparison, string representation, and hashing.

    Example:
        >>> import uuid
        >>>
        >>> # Using as a simple UUID wrapper
        >>> user_uuid = Uuid("123e4567-e89b-12d3-a456-426614174000")
        >>> user_uuid.value
        '123e4567-e89b-12d3-a456-426614174000'
        >>> str(user_uuid)
        '123e4567-e89b-12d3-a456-426614174000'
        >>>
        >>> # Creating from generated UUID
        >>> generated_id = str(uuid.uuid4())
        >>> entity_id = Uuid(generated_id)
        >>>
        >>> class UserId(Uuid):
        ...     @validate
        ...     def _validate_version(self, value: str) -> None:
        ...         parsed_uuid = UUID(value)
        ...         if parsed_uuid.version != 4:
        ...             raise ValueError("Only UUID version 4 allowed")
        ...
        >>> user_id = UserId("123e4567-e89b-12d3-a456-426614174000")
    """

    @validate
    def _ensure_has_value(self, value: str) -> None:
        """
        Validate that the provided value is not None.

        This validator ensures that required UUID values are provided
        and prevents None values from being stored in the value object.

        Args:
            value: The UUID string value to validate.

        Raises:
            RequiredValueError: If the value is None.

        Example:
            >>> Uuid("123e4567-e89b-12d3-a456-426614174000")  # Valid
            Uuid('123e4567-e89b-12d3-a456-426614174000')
            >>> # Uuid(None)  # Would raise RequiredValueError
        """
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_string(self, value: str) -> None:
        """
        Validate that the provided value is of string type.

        This validator ensures type safety by checking that the value
        is actually a string. This prevents other types like UUID objects,
        integers, or other objects from being accepted.

        Args:
            value: The value to validate for string type.

        Raises:
            IncorrectValueTypeError: If the value is not a string.

        Example:
            >>> Uuid("123e4567-e89b-12d3-a456-426614174000")  # Valid string
            Uuid('123e4567-e89b-12d3-a456-426614174000')
            >>> # import uuid
            >>> # Uuid(uuid.uuid4())  # Would raise IncorrectValueTypeError (UUID object)
            >>> # Uuid(123456)  # Would raise IncorrectValueTypeError (integer)
        """
        if not isinstance(value, str):
            raise IncorrectValueTypeError(value)

    @validate
    def _ensure_value_has_valid_uuid_format(self, value: str) -> None:
        """
        Validate that the provided string value is in valid UUID format.

        This validator ensures that the string can be parsed as a valid UUID
        according to RFC 4122. It accepts UUIDs in various formats including
        with or without hyphens.

        Args:
            value: The string value to validate for UUID format.

        Raises:
            InvalidIdFormatError: If the value is not a valid UUID format.

        Example:
            >>> # Valid UUID formats
            >>> Uuid("123e4567-e89b-12d3-a456-426614174000")  # Standard format
            Uuid('123e4567-e89b-12d3-a456-426614174000')
            >>> Uuid("123e4567e89b12d3a456426614174000")  # Without hyphens
            Uuid('123e4567e89b12d3a456426614174000')
            >>>
            >>> # Invalid formats would raise InvalidIdFormatError:
            >>> # Uuid("not-a-uuid")  # Would raise InvalidIdFormatError
            >>> # Uuid("123e4567-e89b-12d3-a456")  # Would raise InvalidIdFormatError (too short)
            >>> # Uuid("gggggggg-gggg-gggg-gggg-gggggggggggg")  # Would raise InvalidIdFormatError (invalid hex)
        """
        try:
            UUID(value)
        except ValueError:
            raise InvalidIdFormatError
