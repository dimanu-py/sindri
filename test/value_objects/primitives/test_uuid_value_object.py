import pytest
from expects import expect, equal, raise_error

from value_object.errors.incorrect_value_type_error import (
    IncorrectValueTypeError,
)
from value_object.errors.invalid_id_format_error import (
    InvalidIdFormatError,
)
from value_object.errors.required_value_error import RequiredValueError
from value_object.value_objects.primitives.uuid import (
    Uuid,
)
from test.mothers.uuid_primitives_mother import (
    UuidPrimitivesMother,
)

pytestmark = pytest.mark.unit


def test_should_create_uuid_value_object() -> None:
    value = UuidPrimitivesMother.any()

    uuid = Uuid(value)

    expect(uuid.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: Uuid(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_string() -> None:
    expect(lambda: Uuid(123)).to(raise_error(IncorrectValueTypeError))


def test_should_raise_error_when_value_is_not_valid_uuid() -> None:
    invalid_uuid = UuidPrimitivesMother.invalid()
    expect(lambda: Uuid(invalid_uuid)).to(raise_error(InvalidIdFormatError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = UuidPrimitivesMother.any()
    first_uuid = Uuid(common_value)
    second_uuid = Uuid(common_value)

    expect(first_uuid).to(equal(second_uuid))


def test_should_not_be_equal_with_different_values() -> None:
    first_uuid = Uuid(UuidPrimitivesMother.any())
    second_uuid = Uuid(UuidPrimitivesMother.any())

    expect(first_uuid).to_not(equal(second_uuid))
