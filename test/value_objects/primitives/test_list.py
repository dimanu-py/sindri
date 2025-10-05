from typing import Any

import pytest
from expects import expect, equal, raise_error

from src.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from src.errors.required_value_error import RequiredValueError
from src.value_objects.primitives.list import (
    List,
)
from test.mothers.primitives.list_primitives_mother import (
    ListPrimitivesMother,
)

pytestmark = pytest.mark.unit


class IntList(List[int]):
    pass


class StringList(List[str]):
    pass


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(ListPrimitivesMother.any_int_list(), id="random int list"),
        pytest.param(ListPrimitivesMother.empty_list(), id="empty list"),
        pytest.param(ListPrimitivesMother.single_item_list(), id="single item list"),
        pytest.param(ListPrimitivesMother.multiple_items_list(), id="multiple items list"),
        pytest.param([1, 2, 3, 4, 5], id="sequential numbers"),
    ],
)
def test_should_create_int_list_value_object(value: list[int]) -> None:
    list_obj = IntList(value)

    expect(list_obj.value).to(equal(value))


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(ListPrimitivesMother.any_string_list(), id="random string list"),
        pytest.param([], id="empty string list"),
        pytest.param(["hello"], id="single string list"),
        pytest.param(["hello", "world", "test"], id="multiple strings list"),
    ],
)
def test_should_create_string_list_value_object(value: list[str]) -> None:
    list_obj = StringList(value)

    expect(list_obj.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: IntList(None)).to(raise_error(RequiredValueError))


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(42, id="integer value"),
        pytest.param("hello", id="string value"),
        pytest.param(3.14, id="float value"),
        pytest.param(True, id="boolean value"),
        pytest.param({}, id="dict value"),
        pytest.param(object(), id="object value"),
    ],
)
def test_should_raise_error_when_value_has_invalid_type(invalid_value: Any) -> None:
    expect(lambda: IntList(invalid_value)).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = ListPrimitivesMother.any_int_list()
    first_list = IntList(common_value)
    second_list = IntList(common_value)

    expect(first_list).to(equal(second_list))


def test_should_not_be_equal_with_different_values() -> None:
    first_list = IntList([1, 2, 3])
    second_list = IntList([4, 5, 6])

    expect(first_list).to_not(equal(second_list))


def test_should_not_allow_to_modify_value() -> None:
    value = ListPrimitivesMother.any_int_list()
    list_obj = IntList(value)

    def modify_value() -> None:
        list_obj._value = [99, 88, 77]

    expect(modify_value).to(raise_error(AttributeError))
