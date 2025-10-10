from src.value_crafter.mothers.object_mother import ObjectMother


class IntPrimitivesMother(ObjectMother):
    @classmethod
    def any(cls) -> int:
        return cls._faker().random_int()

    @classmethod
    def create(cls, is_positive: bool | None = None, min_value: int = -10000, max_value: int = 1000) -> int:
        if is_positive:
            return cls._faker().random_int(min=1, max=abs(max_value))

        if is_positive is False:
            return cls._faker().random_int(min=-abs(min_value), max=-1)

        return cls._faker().random_int(min=min_value, max=max_value)

    @classmethod
    def positive(cls) -> int:
        return cls._faker().random_int(min=1)

    @classmethod
    def negative(cls) -> int:
        return cls._faker().random_int(min=-(2**31), max=-1)

    @staticmethod
    def zero() -> int:
        return 0
