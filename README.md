# 📦 Pydantic for Python Developers

A hands-on tutorial repository for learning Pydantic from basics to advanced validation techniques used in modern Python applications, FastAPI services, and Machine Learning APIs.

## 📖 About

This repository contains practical examples demonstrating how to use Pydantic for:

* Data validation
* Type checking
* Serialization and deserialization
* API request validation
* Environment configuration management
* Nested models
* Custom validators
* Production-grade data handling

Pydantic is widely used in FastAPI and modern Python applications to ensure data integrity and improve developer productivity.

---

## 🚀 What You'll Learn

* Creating Pydantic models
* Field validation
* Optional and default values
* Nested models
* Custom validators
* Model serialization
* Model inheritance
* Settings management
* Working with JSON data
* Integrating Pydantic with FastAPI

---

## 🛠 Tech Stack

* Python 3.11+
* Pydantic v2
* FastAPI
* Uvicorn
* Pytest

---

## 📂 Project Structure

```bash
pydantic-tutorials/
│
├── tutorials/
│   ├── 01_basics/
│   ├── 02_field_types/
│   ├── 03_optional_fields/
│   ├── 04_nested_models/
│   ├── 05_custom_validators/
│   ├── 06_serialization/
│   ├── 07_settings_management/
│   ├── 08_model_inheritance/
│   └── 09_fastapi_integration/
│
├── examples/
│   ├── user_schema.py
│   ├── product_schema.py
│   └── config_schema.py
│
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pydantic-tutorials.git

cd pydantic-tutorials
```

Create a virtual environment:

```bash
python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Examples

Navigate to a tutorial:

```bash
cd tutorials/01_basics
```

Run the example:

```bash
python main.py
```

---

## 🧩 Example: Basic Pydantic Model

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    cgpa: float

student = Student(
    name="Harsh",
    age=19,
    cgpa=8.7
)

print(student)
```

Output:

```text
name='Harsh' age=19 cgpa=8.7
```

---

## ✅ Validation Example

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int

user = User(
    username="john_doe",
    age="25"
)
```

Pydantic automatically converts compatible data types whenever possible.

---

## 🎯 Learning Outcomes

After completing these tutorials, you will be able to:

* Build robust data models
* Validate user input safely
* Handle API requests efficiently
* Create reusable schemas
* Manage application configuration
* Integrate Pydantic with FastAPI projects
* Write cleaner and more maintainable Python code

---

## 📚 Prerequisites

* Basic Python knowledge
* Understanding of classes and objects
* Familiarity with JSON is helpful

---

## 🔥 Real-World Use Cases

* FastAPI request validation
* Machine Learning input schemas
* Configuration management
* Data pipelines
* ETL workflows
* Backend services
* Agentic AI systems
* RAG applications

---

## 🤝 Contributing

Contributions are welcome.

If you find a bug, have a suggestion, or want to add new examples, feel free to open an issue or submit a pull request.

---

## ⭐ Support

If this repository helped you learn Pydantic, consider giving it a star.

Happy coding!
# Data-Validation---Pydantic
