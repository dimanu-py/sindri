import pytest
from typing import Any
from expects import expect, equal, raise_error

from src.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from src.errors.required_value_error import RequiredValueError
from src.value_objects.primitives.float import (
    Float,
)
from test.mothers.float_primitives_mother import (
    FloatPrimitivesMother,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(FloatPrimitivesMother.any(), id="random value"),
        pytest.param(FloatPrimitivesMother.positive(), id="positive value"),
        pytest.param(FloatPrimitivesMother.negative(), id="negative value"),
        pytest.param(FloatPrimitivesMother.zero(), id="zero value"),
    ],
)
def test_should_create_float_value_object(value: float) -> None:
    float_obj = Float(value)

    expect(float_obj.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Float(None)).to(raise_error(RequiredValueError))


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(42, id="integer value"),
        pytest.param("3.14", id="string value"),
    ],
)
def test_should_raise_error_when_value_has_invalid_type(invalid_value: Any) -> None:
    expect(lambda: Float(invalid_value)).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = FloatPrimitivesMother.any()
    first_float = Float(common_value)
    second_float = Float(common_value)

    expect(first_float).to(equal(second_float))


def test_should_not_be_equal_with_different_values() -> None:
    first_float = Float(FloatPrimitivesMother.positive())
    second_float = Float(FloatPrimitivesMother.negative())

    expect(first_float).to_not(equal(second_float))


def test_should_maintain_immutability() -> None:
    value = FloatPrimitivesMother.any()
    float_obj = Float(value)

    def modify_value() -> None:
        float_obj._value = value + 1.0

    expect(modify_value).to(raise_error(AttributeError))
