# if you use the once model inside the other model as field, we call it nested model

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {"city": "multan", "state": "punjab", "pin": "12321"}

address1 = Address(**address_dict)

patient_dict = {
    "name": "abdullha",
    "gender": "male",
    "age": 35,
    "address": address1
}


patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump()
temp2 = patient1.model_dump_json()
print(temp1)
print(temp2)
print(type(temp1))
print(type(temp2))

# print(patient1)
# print(patient1.name)
# print(patient1.age)
# print(patient1.address)
