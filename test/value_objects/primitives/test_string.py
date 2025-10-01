import pytest
from expects import expect, equal, raise_error

from value_object.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.primitives.string import (
    String,
)
from test.mothers.string_primitives_mother import (
    StringPrimitivesMother,
)

pytestmark = pytest.mark.unit


def test_should_create_string_value_object() -> None:
    value = StringPrimitivesMother.any()

    string = String(value)

    expect(string.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: String(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_string() -> None:
    expect(lambda: String(123)).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = StringPrimitivesMother.any()
    first_string = String(common_value)
    second_string = String(common_value)

    expect(first_string).to(equal(second_string))


def test_should_not_be_equal_with_different_values() -> None:
    first_string = String(StringPrimitivesMother.any())
    second_string = String(StringPrimitivesMother.any())

    expect(first_string).to_not(equal(second_string))
