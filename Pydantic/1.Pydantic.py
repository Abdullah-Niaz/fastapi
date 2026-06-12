from pydantic import BaseModel
from typing import List, Dict


class Patient(BaseModel):
    """
    A patient model for demonstration purposes."""
    name: str
    age: int
    weight: float
    height: float
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient(patient: Patient):
    """
    Inserts a patient into the database."""
    print(patient.name)
    print(patient.age)
    print("inserted into database")


def update_patient(patient: Patient):
    """Updates a patient in the database."""
    print(patient.name)
    print(patient.age)
    print("updated in database")


# patient_info_right = {
#     "name": "John Doe",
#     "age": 30
# }
# patient_info_wrong = {
#     "name": "John Doe",
#     "age": "thirty"
# }

patient_info_right = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 175.0,
    "allergies": ["pollen", "dust"],
    "cotact_details": {
        "email": "abdullah423@gmail.com",
        "phone": "123-456-7890"
    }
}
patient_info_wrong = {
    "name": "John Doe",
    "age": "thirty",
    "weight": "seventy",
    "height": "one seventy five",
    "allergies": "pollen, dust",
    "cotact_details": {
        "email": "abdullah423@gmail.com",
        "phone": "123-456-7890"
    }
}
patient1 = Patient(**patient_info_right)
# patient2 = Patient(**patient_info_wrong)


insert_patient(patient1)
# insert_patient(patient2)
# update_patient(patient1)
# update_patient(patient2)
