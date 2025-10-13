"""Public facade for value object implementations.

This module re-exports the most common value objects so they can be
imported directly from :mod:`sindri.value_object`.
"""

from src.sindri.value_objects.aggregate import Aggregate
from src.sindri.value_objects.decorators.validation import validate
from src.sindri.value_objects.errors.sindri_validation_error import SindriValidationError
from src.sindri.value_objects.identifiers.string_uuid import StringUuid
from src.sindri.value_objects.primitives.boolean import Boolean
from src.sindri.value_objects.primitives.float import Float
from src.sindri.value_objects.primitives.integer import Integer
from src.sindri.value_objects.primitives.list import List
from src.sindri.value_objects.primitives.string import String
from src.sindri.value_objects.value_object import ValueObject

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
    "SindriValidationError",
]
