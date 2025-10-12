"""Public facade for value object implementations.

This module re-exports the most common value objects so they can be
imported directly from :mod:`value_crafter.value_object`.
"""

from src.value_crafter.value_objects.aggregate import Aggregate
from src.value_crafter.value_objects.decorators.validation import validate
from src.value_crafter.value_objects.errors.value_object_validation_error import ValueObjectValidationError
from src.value_crafter.value_objects.identifiers.string_uuid import StringUuid
from src.value_crafter.value_objects.primitives.boolean import Boolean
from src.value_crafter.value_objects.primitives.float import Float
from src.value_crafter.value_objects.primitives.integer import Integer
from src.value_crafter.value_objects.primitives.list import List
from src.value_crafter.value_objects.primitives.string import String
from src.value_crafter.value_objects.value_object import ValueObject

__all__ = [
    "Aggregate",
    "validate",
    "StringUuid",
    "Boolean",
    "Float",
    "Integer",
    "List",
    "String",
    "ValueObject",
    "ValueObjectValidationError",
]
