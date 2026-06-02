# Sindripy [DEPRECATED]

**This package has been split into two independent packages.**

| Package | PyPI | Documentation |
|---------|------|---------------|
| Value Objects | [`value-object-sindri`](https://pypi.org/project/value-object-sindri/) | [docs](https://dimanu-py.github.io/value-object/home/) |
| Object Mothers | [`object-mother-sindri`](https://pypi.org/project/object-mother-sindri/) | [docs](https://dimanu-py.github.io/object-mother/home/) |

## Why the split?

The `sindripy` package originally contained both the Value Object and Object Mother patterns. To give each pattern its own focus, versioning, and maintenance, they have been separated into independent packages:

- **[value-object-sindri](https://pypi.org/project/value-object-sindri/)** — Value Object pattern implementation for Python and Domain Driven Design applications.
- **[object-mother-sindri](https://pypi.org/project/object-mother-sindri/)** — Object Mother pattern implementation for Python test data generation.

## Using this package (v2.0.0)

`sindripy` v2.0.0 is a transitional release that installs both `value-object-sindri` and `object-mother-sindri` as dependencies. When you import it, you'll see a deprecation warning instructing you to migrate to the new packages.

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
from value_objects import Integer, String
from object_mother import IntegerPrimitivesMother
```

For full documentation, visit:
- [Value Object docs](https://dimanu-py.github.io/value-object/home/)
- [Object Mother docs](https://dimanu-py.github.io/object-mother/home/)
