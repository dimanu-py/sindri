# Sindri

<div align="center">
  <strong>Easy use and customizable implementation for Value Object and Object Mother patterns.</strong>
</div>

!!! tip "Created with Instant Python"
    This project was generated using [Instant Python](https://dimanu-py.github.io/instant-python/home/), a fast, easy and reliable project generator for Python projects.

<div align="center"><table><tr><td>
Sindri replaces ad hoc primitives and fragile validators with a consistent Value Object and Aggregate 
toolkit you can adopt quickly. 
Spin up validated value objects, aggregates, and test data with a simple and a small, focused API.

Sindri provides a basic-high-customizable implementation to help you enforce
domain invariants and improve code quality with minimal effort.

<br><br>

<b>Why use Sindri?</b> Building your domain with Sindri lets you:

<ul style="list-style-type: none">
  <li>⏱️ Cut domain modeling and validation to seconds</li>
  <li>🛡️ Declare immutable, validated value objects with clear error messages</li>
  <li>🧩 Model aggregates with explicit invariants and composition</li>
  <li>🧪 Generate realistic test data via the Object Mother pattern</li>
  <li>🧰 Start from ready made primitives and identifiers or extend with your own</li>
  <li>🔧 Plug in custom validators, decorators, and typed primitives</li>
</ul>

</td></tr></table></div>

## Documentation

This section provides a high-level overview of the `sindri` library, its features, and how to get started.
For detailed instructions and examples, please refer to the [Value Objects](../value_objects/index.md) 
and [Object Mothers](../object_mothers/index.md) sections.

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Contributing](#contributing)

### Need help?

-   Join a discussion 💬 on [GitHub Discussions]
-   [Raise an issue][GitHub Issues] on GitHub

[GitHub Discussions]: https://github.com/dimanu-py/sindri/discussions
[GitHub Issues]: https://github.com/dimanu-py/sindri/issues

## Installation

The latest version of `sindri` can be installed from PyPI:

```bash
pip install sindripy
```

### Requirements

Sindri tries to support the latest Python versions, we officially support from Python 3.10 to 3.13.
Older versions of Python may work, but they are not guaranteed to be compatible.

## Basic Usage

Here is a simple example of how to use `sindri` to create a value object and generate test data using an object mother.

```python
from sindri.value_objects import Integer, String

age = Integer(30)
name = String("John Doe")

print(f"Name: {name.value}, Age: {age.value}")
```

```python
from sindri.mothers import IntegerPrimitivesMother, StringPrimitivesMother

random_age = IntegerPrimitivesMother.any()
random_name = StringPrimitivesMother.any()
```

!!! note "Learn More"
    To learn more about advanced usage of value objects, including validation, custom value objects,
    complex objects like aggregates, visit the [Value Objects](../value_objects/index.md)
    and [Object Mothers](../object_mothers/index.md) sections.

## Contributing

We welcome contributions to `sindri`! If you have ideas, suggestions, or improvements, please check out our
[contributing guide](contributing_guide.md) for details on how to get involved.
