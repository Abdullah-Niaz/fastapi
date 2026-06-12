def insert_patient(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            print(name)
            print(age)
            print("inserted into database")
    else:
        raise TypeError(
            "Invalid input types: name must be a string and age must be an integer")


insert_patient("John Doe", 20)


def insert_patient_update(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("updated in database")
    else:
        raise TypeError(
            "Invalid input types: name must be a string and age must be an integer")


insert_patient_update("John Doe", 20)


# def insert_patient(name: str, age: int):
#     print(name)
#     print(age)
#     print("inserted into database")


# insert_patient("John Doe", "30")
