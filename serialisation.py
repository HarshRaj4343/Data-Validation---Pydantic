from pydantic import BaseModel
# Serialization is the process of converting a Python object into a format that can be stored, transmitted, or shared, such as a dictionary or JSON.
class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)
temp2 = patient1.model_dump_json()
print(temp)
print(type(temp))
print(temp2)
print(type(temp2))