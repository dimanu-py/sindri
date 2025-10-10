from faker import Faker


class ObjectMother:
    @classmethod
    def _faker(cls) -> Faker:
        return Faker(use_weighting=False)
