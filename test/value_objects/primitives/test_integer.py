from typing import Any

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


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(IntPrimitivesMother.any(), id="random value"),
        pytest.param(42, id="positive integer"),
        pytest.param(-42, id="negative integer"),
        pytest.param(0, id="zero value"),
        pytest.param(1000000, id="large integer"),
    ],
)
def test_should_create_integer_value_object(value: int) -> None:
    integer = Integer(value)

    expect(integer.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Integer(None)).to(raise_error(RequiredValueError))


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(12.34, id="float value"),
        pytest.param("42", id="string value"),
        pytest.param([], id="list value"),
        pytest.param({}, id="dict value"),
    ],
)
def test_should_raise_error_when_value_has_invalid_type(invalid_value: Any) -> None:
    expect(lambda: Integer(invalid_value)).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = IntPrimitivesMother.any()
    first_integer = Integer(common_value)
    second_integer = Integer(common_value)

    expect(first_integer).to(equal(second_integer))


def test_should_not_be_equal_with_different_values() -> None:
    first_integer = Integer(42)
    second_integer = Integer(24)

    expect(first_integer).to_not(equal(second_integer))
