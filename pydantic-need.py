from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Base Model - the main parent class
# EmailStr - used specifically for validating an email
"""AnyUrl serves as the base type for validating and parsing URLs, requiring a valid host component by default while supporting various schemes. It is part of a suite of network types, including HttpUrl and FileUrl, that offer specific scheme and format constraints."""

# Field - used to customize and add metadata to individual model attributes.
# Optional - to make a optional field
# Annotated - Also used to beautify the FastAPI documentations and add the hintings of fields

# Setting strict=True in Pydantic disables automatic type coercion, forcing the validator to throw a ValidationError if the incoming data type does not exactly match the type hint


# '**' unpacks a dictionary into keyword arguments, so each key-value pair in patient_info is passed as a separate field to the Patient model.

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: Annotated[int, Field(min=18, max=120)]
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)