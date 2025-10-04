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


def test_should_create_boolean_value_object() -> None:
    value = BooleanPrimitivesMother.any()

    boolean_obj = Boolean(value)

    expect(boolean_obj.value).to(equal(value))


def test_should_create_boolean_value_object_with_true() -> None:
    value = BooleanPrimitivesMother.true()

    boolean_obj = Boolean(value)

    expect(boolean_obj.value).to(equal(True))


def test_should_create_boolean_value_object_with_false() -> None:
    value = BooleanPrimitivesMother.false()

    boolean_obj = Boolean(value)

    expect(boolean_obj.value).to(equal(False))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Boolean(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_boolean() -> None:
    expect(lambda: Boolean(1)).to(raise_error(IncorrectValueTypeError))


def test_should_raise_error_when_value_is_zero() -> None:
    expect(lambda: Boolean(0)).to(raise_error(IncorrectValueTypeError))


def test_should_raise_error_when_value_is_string() -> None:
    expect(lambda: Boolean("true")).to(raise_error(IncorrectValueTypeError))


def test_should_raise_error_when_value_is_string_false() -> None:
    expect(lambda: Boolean("false")).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = BooleanPrimitivesMother.true()
    first_boolean = Boolean(common_value)
    second_boolean = Boolean(common_value)

    expect(first_boolean).to(equal(second_boolean))


def test_should_not_be_equal_with_different_values() -> None:
    first_boolean = Boolean(BooleanPrimitivesMother.true())
    second_boolean = Boolean(BooleanPrimitivesMother.false())

    expect(first_boolean).to_not(equal(second_boolean))


def test_should_maintain_immutability() -> None:
    value = BooleanPrimitivesMother.any()
    boolean_obj = Boolean(value)

    def modify_value() -> None:
        boolean_obj._value = not value

    expect(modify_value).to(raise_error(AttributeError))


def test_should_distinguish_between_boolean_and_truthy_values() -> None:
    expect(lambda: Boolean(1)).to(raise_error(IncorrectValueTypeError))
    expect(lambda: Boolean(0)).to(raise_error(IncorrectValueTypeError))


def test_should_not_accept_empty_collections_as_valid_booleans() -> None:
    expect(lambda: Boolean([])).to(raise_error(IncorrectValueTypeError))
    expect(lambda: Boolean({})).to(raise_error(IncorrectValueTypeError))
    expect(lambda: Boolean("")).to(raise_error(IncorrectValueTypeError))
