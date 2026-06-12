# Why Do We Need Pydantic?

# Python is Dynamically Typed

from pydantic import BaseModel, Field
Python is a dynamically typed programming language.

When we write:

```python
x = 20
```

Python automatically:

1. Creates an integer object(`20`)
2. Stores it in memory
3. Assigns a reference to the variable `x`

The variable does not store the actual value. It stores a reference to the object.

---

# The Problem

Consider a function that inserts a patient into a database.

```python


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
            "Invalid input types: name must be a string and age must be an integer"
        )


```

Even though we wrote:

```python
name: str
age: int
```

Python does not enforce these types at runtime.

A user can still pass:

```python
insert_patient(123, "hello")
```

Therefore, we must manually validate:

* Input types
* Input values
* Business rules

before storing data in the database.

---

# Manual Validation Creates Boilerplate

For every function we may write:

```python
if type(name) != str:
    raise TypeError()

if type(age) != int:
    raise TypeError()

if age < 0:
    raise ValueError()
```

Now imagine a real-world patient system:

```python
name
age
email
phone
height
weight
gender
blood_group
address
city
country
```

For every field we would need validation logic.

The code quickly becomes repetitive and difficult to maintain.

---

# Enter Pydantic

Pydantic was created to solve this problem.

Instead of writing validation logic inside every function, we define a schema that describes:

* What fields exist
* What types they should have
* What validation rules they must satisfy

Example:

```python


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)


```

Now Pydantic automatically handles validation.

---

# Type Validation

```python
patient = Patient(
    name=123,
    age="abc"
)
```

Pydantic raises a validation error because:

* `name` is not a string
* `age` is not an integer

---

# Data Validation

```python
patient = Patient(
    name="John",
    age=-5
)
```

Pydantic raises a validation error because:

```python
age > 0
```

is required.

---

# Data Parsing

Pydantic can also convert compatible values automatically.

Input:

```python
Patient(age="20")
```

Output:

```python
Patient(age=20)
```

The string is converted into an integer automatically.

This process is called ** parsing ** or **type coercion**.

---

# Why Pydantic Is Important in FastAPI

FastAPI uses Pydantic as its validation engine.

When a client sends:

```json
{
    "name": "John",
    "age": 20
}
```

FastAPI:

1. Receives the JSON data
2. Creates a Pydantic object
3. Validates all fields
4. Returns errors automatically if validation fails
5. Calls the route function only when data is valid

Example:

```python


class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)


```

```python


@app.post("/patients")
def create_patient(patient: PatientCreate):
    return {"message": "Patient created"}


```

No manual validation is required.

---

# Benefits of Pydantic

# 1. Eliminates Boilerplate Code

No need to repeatedly write:

```python
if type(...)
if value invalid
```

---

# 2. Centralized Validation

Validation rules are defined once in the schema.

```python


class Patient(BaseModel):
    ...


```

Every endpoint can reuse the same rules.

---

# 3. Automatic Error Responses

FastAPI automatically returns validation errors.

Example:

```json
{
    "detail": [
        {
            "loc": ["body", "age"],
            "msg": "Input should be greater than 0"
        }
    ]
}
```

---

# 4. Cleaner Business Logic

Route functions focus on:

* Business logic
* Database operations
* Service calls

instead of validation.

---

# Mental Model

Think of Pydantic as a gatekeeper.

```text
Client Request
↓
Pydantic Schema
↓
Validated Python Object
↓
Business Logic
↓
Database
```

Only valid data is allowed to enter the application.

This is the primary reason Pydantic is heavily used with FastAPI and modern Python backend development.
