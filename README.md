# Sindripy [DEPRECATED]

**This package has been split into two independent packages.**

| Package        | PyPI                                                                     | Documentation                                           |
|----------------|--------------------------------------------------------------------------|---------------------------------------------------------|
| Value Objects  | [`value-object-sindri`](https://pypi.org/project/value-object-sindri/)   | [docs](https://dimanu-py.github.io/value-objects/home/) |
| Object Mothers | [`object-mother-sindri`](https://pypi.org/project/object-mother-sindri/) | [docs](https://dimanu-py.github.io/object-mother/home/) |

## What is this?

`sindripy` v2.0.0 is a transitional release that installs `value-object-sindri` and `object-mother-sindri` as dependencies and shows a deprecation warning on import. It no longer contains any implementation.

## Migration

1. Replace `sindripy` with the new packages:

```bash
pip uninstall sindripy
pip install value-object-sindri object-mother-sindri
```

2. Update your imports:

```python
# Old
from sindripy.value_objects import Integer, String
from sindripy.mothers import IntegerPrimitivesMother

# New
from value_object import Integer, String
from object_mother import IntegerPrimitivesMother
```

3. For custom value objects and validators, update the base class imports:

```python
# Old
from sindripy.value_objects.value_object import ValueObject
from sindripy.value_objects.decorators.validation import validate

# New
from value_object import ValueObject, validate
```

For full documentation, visit:
- [Value Objects docs](https://dimanu-py.github.io/value-objects/home/)
- [Object Mother docs](https://dimanu-py.github.io/object-mother/home/)
