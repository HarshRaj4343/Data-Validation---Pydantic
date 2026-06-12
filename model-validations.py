from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

"""
`@model_validator`

* Validates the **entire model at once**, allowing you to check relationships between multiple fields.
* Used when validation depends on combinations of fields (e.g., ensuring a married patient has spouse information).

"""

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)

"""
# When to Use `@classmethod` in Pydantic

- **`@field_validator`**
  - Runs before the model object exists.
  - Uses `cls` because there is no `self` yet.

```python
@field_validator('email')
@classmethod
def validate_email(cls, value):
    ...
```

- **`@model_validator(mode='before')`**
  - Runs before the model object is created.
  - Uses `cls` and receives raw input data.

```python
@model_validator(mode='before')
@classmethod
def validate_data(cls, data):
    ...
```

- **`@model_validator(mode='after')`**
  - Runs after the model object is created.
  - Uses `self` because the object already exists.

```python
@model_validator(mode='after')
def validate_data(self):
    ...
```

## Intuition

- **Before object creation** → Use the blueprint (`cls`).
- **After object creation** → Use the actual object (`self`).
"""