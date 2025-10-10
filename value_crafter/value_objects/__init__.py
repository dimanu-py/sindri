"""Public facade for value object implementations.

This module re-exports the most common value objects so they can be
imported directly from :mod:`value_crafter.value_object`.
"""

from value_crafter.value_objects.aggregate import Aggregate
from value_crafter.value_objects.decorators.validation import validate
from value_crafter.value_objects.identifiers.string_uuid import StringUuid
from value_crafter.value_objects.primitives.boolean import Boolean
from value_crafter.value_objects.primitives.float import Float
from value_crafter.value_objects.primitives.integer import Integer
from value_crafter.value_objects.primitives.list import List
from value_crafter.value_objects.primitives.string import String
from value_crafter.value_objects.value_object import ValueObject
from value_crafter.value_objects.errors.validation_error import ValidationError

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
    "ValidationError",
]
