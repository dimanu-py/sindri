"""Deprecated package.

sindripy has been split into two independent packages:
- value-object-sindri: https://pypi.org/project/value-object-sindri/
- object-mother-sindri: https://pypi.org/project/object-mother-sindri/

Install them directly instead of sindripy.
"""

import warnings

__version__ = "1.0.1"

warnings.warn(
    "sindripy is deprecated. Use 'value-object-sindri' (for Value Objects) "
    "and 'object-mother-sindri' (for Object Mothers) instead. "
    "See https://github.com/dimanu-py/sindri for migration instructions.",
    FutureWarning,
    stacklevel=2,
)
