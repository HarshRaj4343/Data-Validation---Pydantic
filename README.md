# Data Validation with Pydantic

A hands-on repository demonstrating the core features of **Pydantic v2** for data validation, serialization, computed fields, and model design in Python.

This repository is intended for beginners and intermediate developers who want to learn how Pydantic can be used to create robust, type-safe applications with minimal code.

---

## What is Pydantic?

Pydantic is a Python library that uses type hints to perform data validation, parsing, and serialization automatically.

It helps developers:

* Validate incoming data
* Convert data types automatically
* Enforce constraints on fields
* Create nested data structures
* Serialize objects into JSON and dictionaries
* Build reliable APIs with FastAPI

---

## Topics Covered

### 1. Why Pydantic?

File: `pydantic-need.py`

Learn:

* Problems with manual validation
* Type safety
* Automatic type conversion
* Cleaner and more maintainable code

---

### 2. Field Validators

File: `field-validators.py`

Learn:

* Custom field validation
* Data transformation
* Domain-specific validation
* Validation modes (`before` and `after`)

Example:

```python
@field_validator("email")
@classmethod
def validate_email(cls, value):
    ...
```

---

### 3. Model Validators

File: `model-validations.py`

Learn:

* Validation across multiple fields
* Interdependent field checks
* Business logic validation

Example:

```python
@model_validator(mode="after")
def validate_emergency_contact(self):
    ...
```

---

### 4. Nested Models

File: `nested-models.py`

Learn:

* Composing models inside other models
* Deep validation
* Structured data representation

Example:

```python
class Address(BaseModel):
    city: str

class Patient(BaseModel):
    address: Address
```

---

### 5. Computed Fields

File: `computed-fields.py`

Learn:

* Dynamically calculated properties
* Derived values
* Using `@computed_field`
* Using `@property`

Example:

```python
@computed_field
@property
def bmi(self):
    return self.weight / (self.height ** 2)
```

---

### 6. Serialization

File: `serialisation.py`

Learn:

* Converting models to dictionaries
* Converting models to JSON
* Exporting validated data

Examples:

```python
patient.model_dump()
```

```python
patient.model_dump_json()
```

---

## Project Structure

```text
.
├── computed-fields.py
├── field-validators.py
├── model-validations.py
├── nested-models.py
├── pydantic-need.py
├── serialisation.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HarshRaj4343/Data-Validation---Pydantic.git
```

Move into the project directory:

```bash
cd Data-Validation---Pydantic
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Key Pydantic Concepts

| Concept         | Purpose                            |
| --------------- | ---------------------------------- |
| BaseModel       | Base class for all Pydantic models |
| Field           | Add constraints and metadata       |
| field_validator | Validate individual fields         |
| model_validator | Validate multiple fields together  |
| computed_field  | Create derived fields              |
| model_dump      | Convert model to dictionary        |
| model_dump_json | Convert model to JSON              |
| EmailStr        | Email validation                   |
| AnyUrl          | URL validation                     |

---

## Requirements

* Python 3.10+
* Pydantic v2

Install manually:

```bash
pip install pydantic
pip install email-validator
```

---

## Learning Outcome

After completing this repository, you will be able to:

* Build strongly typed data models
* Perform custom data validation
* Create nested schemas
* Implement business logic validations
* Generate computed fields
* Serialize models efficiently
* Prepare for FastAPI development

---

## References

* Pydantic Documentation: https://docs.pydantic.dev
* FastAPI Documentation: https://fastapi.tiangolo.com

---

## License

This repository is intended for educational purposes and personal learning.
