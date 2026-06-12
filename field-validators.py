from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Field_validators are used to do custom data validations.
# @classmethod tells Python that this function belongs to the Patient class, not a specific patient object.
# Pydantic runs validators before creating the Patient object, so self doesn't exist yet.
# Intuitively: the Patient blueprint (cls) checks whether the data is valid before allowing a new patient to be built.

"""
mode="before"

* Runs **before Pydantic converts the data type**, so it receives the raw input exactly as provided by the user.
* Use it when you want to clean, transform, or validate incoming data before parsing.

### `mode="after"` (default)

* Runs **after Pydantic has converted the data to the correct type**, so it receives a validated Python object.
* Use it when your validation logic depends on the final parsed value (e.g., checking that an `age` integer is between 0 and 100).

"""



class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    # Transformation
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)