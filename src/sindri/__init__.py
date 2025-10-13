"""Top level package for the value-crafter library.

This module exposes the most common entry points so the public API is
available through the ``sindri`` namespace when the library is
installed as a dependency.
"""

from src.sindri import mothers, value_objects

__all__ = ["mothers", "value_objects"]
__version__ = "0.0.1"
