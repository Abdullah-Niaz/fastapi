from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float = Field(gt=0)
    height: float = Field(gt=0)
    linkedin_url: AnyUrl
    contact_details: Optional[str] = None

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)


patient_info_right = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "weight": 75.2,
    "height": 1.72,
    "linkedin_url": "https://www.linkedin.com/in/johndoe",
    "contact_details": "John Doe - 555-1234",
}
patient_info_wrong = {
    "name": "John Doe",
    "age": "thirty",
    "email": "john.doe@invalid.com",
    "linkedin_url": "https://www.linkedin.com/in/johndoe",
    "contact_details": "John Doe - 555-1234"
}


def patientdata(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.calculate_bmi)
    print("inserted into database")


patient1 = Patient(**patient_info_right)
# patient2 = Patient(**patient_info_wrong)
# print(patient1)

patientdata(patient1)
