import pytest
from expects import expect, equal, raise_error

from src.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from src.errors.required_value_error import RequiredValueError
from src.value_objects.primitives.integer import (
    Integer,
)
from test.mothers.int_primitives_mother import (
    IntPrimitivesMother,
)

pytestmark = pytest.mark.unit


def test_should_create_int_value_object() -> None:
    value = IntPrimitivesMother.any()

    integer = Integer(value)

    expect(integer.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Integer(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_integer() -> None:
    expect(lambda: Integer("123")).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = IntPrimitivesMother.any()
    first_integer = Integer(common_value)
    second_integer = Integer(common_value)

    expect(first_integer).to(equal(second_integer))


def test_should_not_be_equal_with_different_values() -> None:
    first_integer = Integer(IntPrimitivesMother.any())
    second_integer = Integer(IntPrimitivesMother.any())

    expect(first_integer).to_not(equal(second_integer))
