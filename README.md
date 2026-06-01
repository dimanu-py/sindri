# Sindri: Value Objects & Object Mother

### Value Object and Object Mother patterns for Python and Domain Driven Design applications

Easy use and customizable implementation for Value Object and Object Mother patterns, split into two independent packages.

<p align="center">
  <a href="https://dimanu-py.github.io/sindri/getting_started/">Getting Started</a>&nbsp;&nbsp;•&nbsp;
  <a href="https://dimanu-py.github.io/sindri/value_objects/">Value Object Pattern</a>&nbsp;&nbsp;•&nbsp;
  <a href="https://dimanu-py.github.io/sindri/object_mothers/">Object Mother Pattern</a>
</p>

<div align="center"><table><tr><td>
Sindri replaces ad hoc primitives and fragile validators with a consistent Value Object and Aggregate 
toolkit you can adopt quickly. 
Spin up validated value objects, aggregates, and test data with a simple and a small, focused API.

The project provides two independent packages: **`value-object-sindri`** (zero runtime dependencies) for value
object patterns and **`object-mother-sindri`** (depends on faker) for test data generation.

<br>

<b>Why use them?</b> Building your domain with Sindri lets you:

<ul style="list-style-type: none">
  <li>⏱️ Cut domain modeling and validation to seconds</li>
  <li>🛡️ Declare immutable, validated value objects with clear error messages</li>
  <li>🧩 Model aggregates with explicit invariants and composition</li>
  <li>🧪 Generate realistic test data via the Object Mother pattern</li>
  <li>🧰 Start from ready made primitives and identifiers or extend with your own</li>
  <li>🔧 Plug in custom validators, decorators, and typed primitives</li>
</ul>

</td></tr></table></div>

<div style="background-color: #1e2d3d; border: 1px solid #00d9ff; border-radius: 8px; padding: 16px; margin: 16px 0; display: flex; align-items: flex-start; gap: 12px;">
  <div style="font-size: 20px; color: #00d9ff; flex-shrink: 0;">💧</div>
  <div>
    <strong style="color: #00d9ff;">Created with Instant Python</strong><br>
    <span style="color: #a0a0a0;">This project was generated using <a href="https://github.com/dimanu-py/instant-python" style="color: #00d9ff; text-decoration: none;">Instant Python</a>, a fast, easy and reliable project generator for Python projects.</span>
  </div>
</div>

## Navigation Guide

This section provides a high-level overview of the documentation so you can find quickly what you need.

### For Users

- [Installation]
- [First Steps]
- [Value Object Pattern]
- [Object Mother Pattern]

### For Developers

- [Contributing Guide]
- [Security Policy]

### Need help?

-   Join a discussion 💬 on [GitHub Discussions]
-   [Raise an issue][GitHub Issues] on GitHub

## Fast Kickstart

Install only what you need:

```bash
pip install value-object-sindri      # zero dependencies
pip install object-mother-sindri      # with faker for test data
```

Here is a simple example of how to use `sindri` to create a value object and generate test data using an object mother.

```python
from value_objects import Integer, String

age = Integer(30)
name = String("John Doe")

print(f"Name: {name.value}, Age: {age.value}")
```

```python
from object_mother import IntegerPrimitivesMother, StringPrimitivesMother

random_age = IntegerPrimitivesMother.any()
random_name = StringPrimitivesMother.any()
```

# Migration Guides

## v2.0.0: Package split

> **⚠️ `sindripy` is deprecated.** Use `value-object-sindri` and `object-mother-sindri` directly.

The monolith `sindripy` package has been split into two independent packages:

- **`value-object-sindri`** — value objects (zero runtime dependencies)
- **`object-mother-sindri`** — object mothers (depends on `faker`)

| Step                   | Before (`sindripy`)                                    | After                                                   |
|------------------------|--------------------------------------------------------|---------------------------------------------------------|
| Install value objects  | `pip install sindripy`                                 | `pip install value-object-sindri`                       |
| Install object mothers | `pip install sindripy[mother]`                         | `pip install object-mother-sindri`                      |
| Import value objects   | `from sindripy.value_objects import Integer`           | `from value_objects import Integer`                     |
| Import mothers         | `from sindripy.mothers import IntegerPrimitivesMother` | `from object_mother import IntegerPrimitivesMother`     |
| pyproject.toml dep     | `"sindripy"`                                           | `"value-object-sindri"` and/or `"object-mother-sindri"` |

Most editors support bulk find-and-replace for import paths, making the migration mechanical:

```
sindripy.value_objects. → value_objects.
sindripy.mothers.       → object_mother.
```

## v1.0.0: Validator signature change

This release includes a breaking change to the validator API used by value objects:

- Validators no longer accept the incoming value as a parameter. Instead, the value is assigned to `self._value` before validators run, and validator methods have the signature `def _validate_xxx(self) -> None:`.
- This simplifies validator signatures and reduces repetition across validation methods.

Why this is a breaking change

- Existing validator methods that still declare a `value` parameter will receive the wrong signature and raise a `TypeError` when the framework calls them. Custom code that expects the old parameter (for example, custom exception constructors or external utilities) may also need small updates.

How to migrate

- Follow the step-by-step migration guide which shows the exact edits and examples: [Validator Signature Migration Guide](docs/documentation/value_objects/migration_guide.md).
- In short: find all methods decorated with `@validate`, remove the `value` parameter, replace uses of `value` with `self._value`, and update any error messages or custom exceptions that referenced the old parameter.

A quick checklist:

- [ ] Update `@validate` methods to `def _... (self) -> None`
- [ ] Replace `value` references with `self._value`
- [ ] Update error messages and custom exception usages
- [ ] Run your tests


<div style="background-color: #1e2d3d; border: 1px solid #00d9ff; border-radius: 8px; padding: 16px; margin: 16px 0; display: flex; align-items: flex-start; gap: 12px;">
  <div style="font-size: 20px; color: #00d9ff; flex-shrink: 0;">ℹ️</div>
  <div>
    <strong style="color: #00d9ff;">Learn More</strong><br>
    <span style="color: #a0a0a0;">To learn more about advanced usage of value objects, including validation, custom value objects, complex objects like aggregates, visit the <a href="https://dimanu-py.github.io/sindri/value_objects/" style="color: #00d9ff; text-decoration: none;">Value Object Pattern</a> and <a href="https://dimanu-py.github.io/sindri/object_mothers" style="color: #00d9ff; text-decoration: none;">Object Mother Pattern</a> sections of the documentation.</span>
  </div>
</div>


[GitHub Discussions]: https://github.com/dimanu-py/sindri/discussions
[GitHub Issues]: https://github.com/dimanu-py/sindri/issues
[Installation]: https://github.com/dimanu-py/sindri/getting_started/installation/
[First Steps]: https://github.com/dimanu-py/sindri/getting_started/first_steps/
[Value Object Pattern]: https://dimanu-py.github.io/sindri/value_objects/
[Object Mother Pattern]: https://dimanu-py.github.io/sindri/object_mothers
[Contributing Guide]: https://github.com/dimanu-py/sindri/contributing/contributing_guide/
[Security Policy]: https://github.com/dimanu-py/sindri/contributing/security/