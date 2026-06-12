# Pydantic
1. Define the Pydantic model(class) that represents the ideal schema of the data.
    * This includes the expected fields(name,age), their types(name:str, age:int), and any vlidation constraints (e.g gt = 0) for positive number
2. Instantiate the model with raw input data (usually a dictionary or JSON-like structure).
    * Pydantic will automatically validate the data and coerce it into the corect python types (if possible).
    * if the data doest not meet the model's requirements, Pydantic raises a ValidationError.
    ```
    pydantic object(validated) = {

        name:ali,
        age: 20
    }
    ```

3. Pass the vallidated model object to function or use it throughout your codebase.
    * This ensures that evry part of your Program works with clean, type-sage, and logically valid data. 



## The Real Flow

```text
Raw JSON / Dictionary
          ↓
Patient(**data)
          ↓
Pydantic Validation
          ↓
Validated Patient Object
          ↓
Service Function
          ↓
Database
```

This is the same flow FastAPI uses internally:

```text
HTTP Request
      ↓
Pydantic Model
      ↓
Validated Object
      ↓
Route Function
      ↓
Service Layer
      ↓
Database
```

So a more accurate summary would be:

1. Create a Pydantic model that defines the schema.
2. Receive raw input data (dict/JSON).
3. Create a `Patient` instance using that data.
4. Pydantic validates and parses the data.
5. If validation succeeds, a validated `Patient` object is created.
6. Pass the validated object to business logic functions.
7. Business logic can assume the data structure and types are correct.
