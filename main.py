from typing import Union

from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc"
)


def load_data():
    with open("patient_data.json", "r") as f:
        return json.load(f)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"description": "This is a simple FastAPI application."}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/contact")
def contact():
    return {"message": "You can contact us at contact@example.com"}


@app.get("/view")
def view():
    data = load_data()
    return {"patient_data": data}


@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="12345")):
    data = load_data()
    if patient_id in data:
        return {"patient_data": data[patient_id]}
    raise HTTPException(status_code=404, detail="patient data not found")


@app.get("/sort/")
def sort_patient(sort_by: str = Query(..., description="sort on the basis of Height Weight, BMO"), order: str = Query("asc", description="sort in asc or desc order")):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f"invalid field select from {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400, detail="invalid order from asc or desc")

    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(
        sort_by, 0), reverse=sort_order)

    return sorted_data
