from abc import ABC

from faker import Faker


class ObjectMother(ABC):

    @classmethod
    def _faker(cls) -> Faker:
        return Faker(use_weighting=False)
