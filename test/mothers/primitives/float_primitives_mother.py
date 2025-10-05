from random import uniform


class FloatPrimitivesMother:
    """Mother class for generating float primitive values for testing."""

    @staticmethod
    def any() -> float:
        """Generate any random float value."""
        return uniform(-1000.0, 1000.0)

    @staticmethod
    def positive() -> float:
        """Generate a positive float value."""
        return uniform(0.1, 1000.0)

    @staticmethod
    def negative() -> float:
        """Generate a negative float value."""
        return uniform(-1000.0, -0.1)

    @staticmethod
    def zero() -> float:
        """Generate zero as a float."""
        return 0.0
