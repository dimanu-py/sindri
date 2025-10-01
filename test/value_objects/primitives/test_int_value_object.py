import pytest
from expects import expect, equal, raise_error

from value_object.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.primitives.int_value_object import (
    IntValueObject,
)
from test.mothers.int_primitives_mother import (
    IntPrimitivesMother,
)

pytestmark = pytest.mark.unit


def test_should_create_int_value_object() -> None:
    value = IntPrimitivesMother.any()

    integer = IntValueObject(value)

    expect(integer.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: IntValueObject(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_integer() -> None:
    expect(lambda: IntValueObject("123")).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = IntPrimitivesMother.any()
    first_integer = IntValueObject(common_value)
    second_integer = IntValueObject(common_value)

    expect(first_integer).to(equal(second_integer))


def test_should_not_be_equal_with_different_values() -> None:
    first_integer = IntValueObject(IntPrimitivesMother.any())
    second_integer = IntValueObject(IntPrimitivesMother.any())

    expect(first_integer).to_not(equal(second_integer))
