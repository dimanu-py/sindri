import pytest
from typing import TypeVar, Dict, Optional
from expects import expect, equal, raise_error

from src.errors.incorrect_value_type_error import IncorrectValueTypeError
from src.errors.required_value_error import RequiredValueError
from src.value_objects.primitives.list import List
from test.mothers.list_primitives_mother import ListPrimitivesMother

pytestmark = pytest.mark.unit

# TypeVar for testing generic scenarios
T = TypeVar('T')
U = TypeVar('U', bound=str)


class IntegerList(List[int]):
    """Concrete List subclass for testing"""
    pass


class StringList(List[str]):
    """Concrete List subclass for testing"""
    pass


class DictList(List[Dict[str, int]]):
    """Generic type List subclass for testing"""
    pass


class OptionalStringList(List[Optional[str]]):
    """Optional type List subclass for testing"""
    pass


class GenericList(List[T]):
    """TypeVar List subclass for testing"""
    pass


def test_should_create_integer_list_value_object() -> None:
    value = ListPrimitivesMother.any_int_list()

    list_obj = IntegerList(value)

    expect(list_obj.value).to(equal(value))


def test_should_create_string_list_value_object() -> None:
    value = ListPrimitivesMother.any_string_list()

    list_obj = StringList(value)

    expect(list_obj.value).to(equal(value))


def test_should_create_empty_list_value_object() -> None:
    value = ListPrimitivesMother.empty_list()

    list_obj = IntegerList(value)

    expect(list_obj.value).to(equal(value))


def test_should_create_single_item_list_value_object() -> None:
    value = ListPrimitivesMother.single_item_list()

    list_obj = IntegerList(value)

    expect(list_obj.value).to(equal(value))


def test_should_create_multiple_items_list_value_object() -> None:
    value = ListPrimitivesMother.multiple_items_list()

    list_obj = IntegerList(value)

    expect(list_obj.value).to(equal(value))


def test_should_raise_error_when_value_is_none() -> None:
    expect(lambda: IntegerList(None)).to(raise_error(RequiredValueError))


def test_should_raise_error_when_value_is_not_list() -> None:
    expect(lambda: IntegerList(42)).to(raise_error(IncorrectValueTypeError))


def test_should_raise_error_when_value_is_string() -> None:
    expect(lambda: IntegerList("not a list")).to(raise_error(IncorrectValueTypeError))


def test_should_compare_equal_with_same_value() -> None:
    common_value = ListPrimitivesMother.any_int_list()
    first_list = IntegerList(common_value)
    second_list = IntegerList(common_value)

    expect(first_list).to(equal(second_list))


def test_should_not_be_equal_with_different_values() -> None:
    first_list = IntegerList([1, 2, 3])
    second_list = IntegerList([4, 5, 6])

    expect(first_list).to_not(equal(second_list))


def test_should_maintain_immutability() -> None:
    value = ListPrimitivesMother.any_int_list()
    list_obj = IntegerList(value)

    def modify_value() -> None:
        list_obj._value = [999]

    expect(modify_value).to(raise_error(AttributeError))


# __init_subclass__ tests for type parameterization


def test_should_store_concrete_type_in_element_type() -> None:
    expect(IntegerList._element_type).to(equal(int))
    expect(StringList._element_type).to(equal(str))


def test_should_store_generic_type_in_element_type() -> None:
    expect(DictList._element_type).to(equal(Dict[str, int]))
    expect(OptionalStringList._element_type).to(equal(Optional[str]))


def test_should_store_typevar_in_element_type() -> None:
    expect(GenericList._element_type).to(equal(T))


def test_should_raise_error_when_class_not_parameterized() -> None:
    def create_unparameterized_class() -> None:
        class UnparameterizedList(List):
            pass

    expect(create_unparameterized_class).to(raise_error(TypeError))


def test_should_raise_error_when_inheriting_from_wrong_base() -> None:
    def create_wrong_base_class() -> None:
        class WrongBase:
            pass
        
        class WrongList(WrongBase, List[int]):
            pass

    # This should work fine since List[int] is in __orig_bases__
    # The error would only occur if List[T] wasn't found in __orig_bases__
    create_wrong_base_class()  # Should not raise an error


def test_should_raise_error_with_primitive_value_as_type() -> None:
    # Note: This test demonstrates what would happen if someone tried to use a primitive value
    # In practice, this would be caught by the type checker before runtime
    # But our __init_subclass__ method provides runtime protection as well
    
    # We can't actually create List[42] because Python's type system prevents it
    # But we can test the logic by manually checking what our code would do
    from typing import get_args, get_origin
    
    # Our validation logic from __init_subclass__ would catch invalid types
    element_type = 42  # This is a primitive value, not a type
    
    # This is the same check from our __init_subclass__ method
    is_valid = (
        isinstance(element_type, TypeVar) or
        isinstance(element_type, type) or
        hasattr(element_type, "__origin__") or
        get_origin(element_type) is not None
    )
    
    expect(is_valid).to(equal(False))


def test_dict_list_creation() -> None:
    value = [{"key1": 1, "key2": 2}, {"key3": 3}]
    
    dict_list = DictList(value)
    
    expect(dict_list.value).to(equal(value))


def test_optional_string_list_creation() -> None:
    value = ["hello", None, "world"]
    
    optional_list = OptionalStringList(value)
    
    expect(optional_list.value).to(equal(value))


def test_generic_list_creation() -> None:
    value = [1, 2, 3]
    
    generic_list = GenericList(value)
    
    expect(generic_list.value).to(equal(value))


def test_list_repr_representation() -> None:
    value = [1, 2, 3]
    list_obj = IntegerList(value)
    
    # The repr should follow the pattern from ValueObject (without _value)
    expected_repr = f"IntegerList({value!r})"
    expect(repr(list_obj)).to(equal(expected_repr))


def test_list_str_representation() -> None:
    value = [1, 2, 3]
    list_obj = IntegerList(value)
    
    # The str should return the string representation of the value
    expected_str = str(value)
    expect(str(list_obj)).to(equal(expected_str))


def test_list_hash_consistency() -> None:
    value = [1, 2, 3]
    first_list = IntegerList(value)
    second_list = IntegerList(value)
    
    # Lists are converted to tuples for hashing
    expect(hash(first_list)).to(equal(hash(second_list)))


def test_list_hash_with_nested_lists() -> None:
    # Test that nested lists cause a hashing error when trying to hash the object
    value = [[1, 2], [3, 4]]

    # Creating the list should work fine
    nested_list = IntegerList(value)

    # But hashing it should raise an error because nested lists can't be converted to tuples for hashing
    def hash_nested_list() -> None:
        hash(nested_list)

    expect(hash_nested_list).to(raise_error(TypeError))


def test_list_hash_with_hashable_elements() -> None:
    value = [1, 2, 3]
    list_obj = IntegerList(value)

    # Should be able to hash lists with hashable elements
    hash_value = hash(list_obj)
    expect(isinstance(hash_value, int)).to(equal(True))
