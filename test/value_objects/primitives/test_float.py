import pytest
from expects import expect, equal, raise_error

from value_object.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.primitives.float import (
    Float,
)
from test.mothers.float_primitives_mother import (
    FloatPrimitivesMother,
)

pytestmark = pytest.mark.unit


def test_should_create_float_value_object() -> None:
    value = FloatPrimitivesMother.any()

    float_obj = Float(value)

    expect(float_obj.value).to(equal(value))


def test_should_create_float_value_object_with_positive_value() -> None:
    value = FloatPrimitivesMother.positive()

    float_obj = Float(value)

    expect(float_obj.value).to(equal(value))


def test_should_create_float_value_object_with_negative_value() -> None:
    value = FloatPrimitivesMother.negative()

    float_obj = Float(value)

    expect(float_obj.value).to(equal(value))


def test_should_create_float_value_object_with_zero() -> None:
    value = FloatPrimitivesMother.zero()

    float_obj = Float(value)

    expect(float_obj.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Float(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_float() -> None:
    expect(lambda: Float(42)).to(raise_error(IncorrectValueTypeError))


def test_should_raise_error_when_value_is_string() -> None:
    expect(lambda: Float("3.14")).to(raise_error(IncorrectValueTypeError))


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
        float_obj._value = 999.999

    expect(modify_value).to(raise_error(AttributeError))
