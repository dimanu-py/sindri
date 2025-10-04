from typing import override, Any, get_origin, get_args, TypeVar

from src.errors.incorrect_value_type_error import IncorrectValueTypeError
from src.errors.required_value_error import RequiredValueError
from src.value_objects.decorators.validation import validate
from src.value_objects.value_object import ValueObject


class List[T](ValueObject[list[T]]):
    _element_type: type | TypeVar | None = None

    @validate
    def _ensure_has_value(self, value: list[T]) -> None:
        """
        Validate that the provided value is not None.

        This validator ensures that required list values are provided
        and prevents None values from being stored in the value object.

        Args:
            value: The list value to validate.

        Raises:
            RequiredValueError: If the value is None.
        """
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_is_list(self, value: list[T]) -> None:
        """
        Validate that the provided value is of list type.

        This validator ensures type safety by checking that the value
        is actually a list. This prevents other types like strings,
        integers, or other objects from being accepted.

        Args:
            value: The value to validate for list type.

        Raises:
            IncorrectValueTypeError: If the value is not a list.
        """
        if not isinstance(value, list):
            raise IncorrectValueTypeError(value)

    @override
    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        # Check __orig_bases__ to find the List parameterization
        if not hasattr(cls, "__orig_bases__") or not getattr(cls, "__orig_bases__", None):
            raise TypeError(f"Class {cls.__name__} must be parameterized with a type argument")

        # Find the List base class in __orig_bases__
        list_base = None
        orig_bases = getattr(cls, "__orig_bases__", ())
        for base in orig_bases:
            if get_origin(base) is List:
                list_base = base
                break

        if list_base is None:
            raise TypeError(f"Class {cls.__name__} must inherit from List[T] with a type parameter")

        # Extract type arguments
        element_type, *_ = get_args(list_base)

        # Handle TypeVar cases: If the type is a generic type, store it directly
        if isinstance(element_type, TypeVar):
            cls._element_type = element_type
            return
        # Validate concrete types: Ensure the type parameter is actually a valid type
        elif isinstance(element_type, type):
            cls._element_type = element_type
            return
        # Handle generic types like list[int], dict[str, int], etc.
        elif hasattr(element_type, "__origin__") or get_origin(element_type) is not None:
            cls._element_type = element_type
            return

        raise TypeError(f"Type parameter must be a valid type, not a primitive value: {element_type}")

    @override
    def __hash__(self) -> int:
        """
        Return the hash value of this value object.

        Since lists are unhashable in Python, we convert the list to a tuple
        for hashing purposes while maintaining the original list value.

        Returns:
            The hash value based on the tuple representation of the list.
        """
        return hash(tuple(self._value))
