from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['example.com', 'test.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Email must be from a valid domain")
        return value

    @field_validator("name", mode='after')
    @classmethod
    def validate_name(cls, value):
        return value.upper()


patient_info_right = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "linkedin_url": "https://www.linkedin.com/in/johndoe"
}
patient_info_wrong = {
    "name": "John Doe",
    "age": "thirty",
    "email": "john.doe@invalid.com",
    "linkedin_url": "https://www.linkedin.com/in/johndoe"
}


def patientdata(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print("inserted into database")


patient1 = Patient(**patient_info_right)
# patient2 = Patient(**patient_info_wrong)
# print(patient1)

patientdata(patient1)
