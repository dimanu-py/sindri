from test.mothers.random_generator import RandomGenerator
from test.mothers.primitives.int_primitives_mother import IntPrimitivesMother
from test.mothers.primitives.string_primitives_mother import StringPrimitivesMother


class ListPrimitivesMother:
    @staticmethod
    def any_int_list() -> list[int]:
        return [IntPrimitivesMother.any() for _ in range(RandomGenerator.positive_integer() % 5 + 1)]

    @staticmethod
    def any_string_list() -> list[str]:
        return [StringPrimitivesMother.any() for _ in range(RandomGenerator.positive_integer() % 5 + 1)]

    @staticmethod
    def empty_list() -> list[int]:
        return []

    @staticmethod
    def single_item_list() -> list[int]:
        return [IntPrimitivesMother.any()]

    @staticmethod
    def multiple_items_list() -> list[int]:
        return [IntPrimitivesMother.any() for _ in range(3)]

    @staticmethod
    def mixed_types_list() -> list:
        return [1, "string", 3.14, True]
