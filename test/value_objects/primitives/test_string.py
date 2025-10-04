from typing import Any

import pytest
from expects import expect, equal, raise_error

from src.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from src.errors.required_value_error import RequiredValueError
from src.value_objects.primitives.string import (
    String,
)
from test.mothers.string_primitives_mother import (
    StringPrimitivesMother,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(StringPrimitivesMother.any(), id="random value"),
        pytest.param("", id="empty string"),
    ],
)
def test_should_create_string_value_object(value: str) -> None:
    string = String(value)

    expect(string.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: String(None)).to(raise_error(RequiredValueError))


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(123, id="integer value"),
        pytest.param(12.34, id="float value"),
        pytest.param(True, id="boolean value"),
    ],
)
def test_should_raise_error_when_value_has_invalid_type(invalid_value: Any) -> None:
    expect(lambda: String(invalid_value)).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = StringPrimitivesMother.any()
    first_string = String(common_value)
    second_string = String(common_value)

    expect(first_string).to(equal(second_string))


def test_should_not_be_equal_with_different_values() -> None:
    first_string = String("hello")
    second_string = String("world")

    expect(first_string).to_not(equal(second_string))
