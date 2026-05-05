# import FastAPI
# FastAPI is the predefined class, used to develp API calls
from fastapi import FastAPI

# import BaseModel from folder/package pydantic
# BaseModel used to define Schema
from pydantic import BaseModel

# typing used to provide restriction
from typing import List

# to connect to MongoDB asynchronously
from motor.motor_asyncio import AsyncIOMotorClient

# instantiate FastAPI
app = FastAPI()

# MongoDB Connection
MONGO_URL = "mongodb+srv://admin:admin@pythonai.phjq8zd.mongodb.net/?appName=PythonAI"

client = AsyncIOMotorClient(MONGO_URL)
db = client["company_db"]
collection = db["employees"]

# ----------------------------------
# Employee BaseModel
# ----------------------------------
class Employee(BaseModel):
    emp_id: int
    emp_name: str
    department: str
    salary: float


# ----------------------------------
# Home API
# ----------------------------------
@app.get("/")
def home():
    return {"message": "Employee CRUD API with MongoDB ..!"}


# ----------------------------------
# POST Employee
# ----------------------------------
@app.post("/employees")
async def add_employee(employee: Employee):

    await collection.insert_one(employee.dict())

    return {
        "message": "Employee Added",
        "data": employee
    }


# ----------------------------------
# GET All Employees
# ----------------------------------
@app.get("/employees", response_model=List[Employee])
async def get_all_employees():

    data = []
    cursor = collection.find()

    async for emp in cursor:
        emp.pop("_id")   # remove MongoDB internal id
        data.append(emp)

    return data


# ----------------------------------
# GET Single Employee
# ----------------------------------
@app.get("/employees/{emp_id}")
async def get_employee(emp_id: int):

    emp = await collection.find_one({"emp_id": emp_id})

    if emp:
        emp.pop("_id")
        return emp

    return {"message": "Employee Not Found"}


# ----------------------------------
# PUT Update Employee
# ----------------------------------
@app.put("/employees/{emp_id}")
async def update_employee(emp_id: int, updated_employee: Employee):

    result = await collection.update_one(
        {"emp_id": emp_id},
        {"$set": updated_employee.dict()}
    )

    if result.modified_count:
        return {
            "message": "Employee Updated",
            "data": updated_employee
        }

    return {"message": "Employee Not Found"}


# ----------------------------------
# DELETE Employee
# ----------------------------------
@app.delete("/employees/{emp_id}")
async def delete_employee(emp_id: int):

    result = await collection.delete_one({"emp_id": emp_id})

    if result.deleted_count:
        return {"message": "Employee Deleted"}

    return {"message": "Employee Not Found"}

