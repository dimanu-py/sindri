from value_crafter.mothers.object_mother import ObjectMother


class ListPrimitivesMother(ObjectMother):
    @staticmethod
    def empty() -> list:
        """Generate an empty list."""
        return []
