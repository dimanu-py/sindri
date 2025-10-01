from random import choice


class BooleanPrimitivesMother:
    """Mother class for generating boolean primitive values for testing."""

    @staticmethod
    def any() -> bool:
        """Generate any random boolean value."""
        return choice([True, False])

    @staticmethod
    def true() -> bool:
        """Generate True value."""
        return True

    @staticmethod
    def false() -> bool:
        """Generate False value."""
        return False
