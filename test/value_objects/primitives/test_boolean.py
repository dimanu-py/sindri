from typing import Any

import pytest
from expects import expect, equal, raise_error

from src.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from src.errors.required_value_error import RequiredValueError
from src.value_objects.primitives.boolean import (
    Boolean,
)
from test.mothers.boolean_primitives_mother import (
    BooleanPrimitivesMother,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(BooleanPrimitivesMother.any(), id="random value"),
        pytest.param(BooleanPrimitivesMother.true(), id="true value"),
        pytest.param(BooleanPrimitivesMother.false(), id="false value"),
    ],
)
def test_should_create_boolean_value_object(value: bool) -> None:
    boolean_obj = Boolean(value)

    expect(boolean_obj.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Boolean(None)).to(raise_error(RequiredValueError))


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(1, id="integer value"),
        pytest.param(0, id="zero value"),
        pytest.param("true", id="truthy string value"),
        pytest.param("false", id="falsy string value"),
        pytest.param("", id="empty falsy string"),
        pytest.param([], id="empty falsy list"),
        pytest.param({}, id="empty falsy dict"),
    ],
)
def test_should_raise_error_when_value_has_invalid_type(invalid_value: Any) -> None:
    expect(lambda: Boolean(invalid_value)).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = BooleanPrimitivesMother.true()
    first_boolean = Boolean(common_value)
    second_boolean = Boolean(common_value)

    expect(first_boolean).to(equal(second_boolean))


def test_should_not_be_equal_with_different_values() -> None:
    true_boolean = Boolean(BooleanPrimitivesMother.true())
    false_boolean = Boolean(BooleanPrimitivesMother.false())

    expect(true_boolean).to_not(equal(false_boolean))


def test_should_not_allow_to_modify_value() -> None:
    value = BooleanPrimitivesMother.any()
    boolean = Boolean(value)

    def modify_value() -> None:
        boolean._value = not value

    expect(modify_value).to(raise_error(AttributeError))
