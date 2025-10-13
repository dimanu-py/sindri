# Getting Started

This page provides a quick start guide for installing and using the `value-crafter` library in your project. 
You will learn how to:

- [Install the library](#installation)
- [Create your first value objects](#creating-value-objects)
- [Generate test data using object mothers](#generate-test-data-using-object-mothers)

If you want to go directly to a detailed explanation of the library's features,
see the [Value Objects](../value_objects/index.md) and [Object Mothers](../object_mothers/index.md) sections.

If you are interested in contributing to the project, visit the [Contributing](../contributing/index.md) section.

## Installation

`value-crafter` requires Python 3.13 and uses uv as its dependency manager.

### Installing with pip

```bash
pip install value-crafter
```

### Installing with uv

```bash
uv add value-crafter
```

The library has no runtime dependencies. All dependencies listed in pyproject.toml
are development dependencies organized into groups: test, lint, release, and dev.

## How To Use

### Creating Value Objects

You can use the [built-in primitive value objects](../value_objects/built_in_vo.md) directly in your code by creating
instances of them.

```python
from value_crafter.value_objects import Integer, Boolean

age = Integer(25)
is_active = Boolean(True)

print(age.value) # 25
print(is_active.value) # True
```

!!! notes "Advanced Usage"
    To learn more about advanced usage of value objects, including validation, custom value objects,
    complex objects like aggregates, visit the [Value Objects](../value_objects/index.md) section.

### Generate Test Data Using Object Mothers

The library provides an easy-to-use API to generate test data using the [Object Mother pattern](../object_mothers/index.md). .

You can use the built-in primitive object mothers directly in your tests:

```python
from value_crafter.mothers import IntPrimitivesMother, BooleanPrimitivesMother

random_age = IntPrimitivesMother.any()
is_active = BooleanPrimitivesMother.true()
```

## Next Steps

Now that you have a basic understanding of how to install and use the `value-crafter` library,
you can explore the following sections for more detailed information:

- [Value Objects](../value_objects/index.md): Learn more about creating and using value objects.
- [Object Mothers](../object_mothers/index.md): Learn more about generating test data using object mothers