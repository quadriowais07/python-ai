# import FastAPI
# FastAPI is the predefined class, used to develp API calls
from fastapi import FastAPI

# import BaseModel from folder/package pydantic
# BaseModel used to define Schema
from pydantic import BaseModel

# instantiate FastAPI
app = FastAPI()

# Define Schema (Rules & Regulations)
class Employee(BaseModel):
    emp_id:int
    emp_name:str
    department:str
    salary:float
    experience:int
    email:str
    is_active:bool

employees = [{
    "emp_id": 111,
    "emp_name": "Emp1",
    "department": "CSE",
    "salary": 10000,
    "experience": 1,
    "email": "emp1@gmail.com",
    "is_active": True 
}]

@app.get("/")
def home():
    return {"message": "welcome to Fast API..!"}

# http://127.0.0.1:8000/docs --- Swagger docs
# http://127.0.0.1:8000/redoc --- 

@app.get("/employees")
def get_all_employees():
    return {
        "total_employees": len(employees),
        "data": employees
    }

# request parameter
@app.get("/employee/{emp_id}")
def get_employee(emp_id:int):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    return {"message": "Employee not found..!"}

# post request
@app.post("/add-employee")
def add_employee(employee: Employee):
    employees.append(employee.model_dump()) #model_dump will convert obj to dictionary
    return {"message": "Employee added successfully..!", "employee":employee}


# PUT
@app.put("/update-employee/{emp_id}")
def update_employee(emp_id:int, updated_employee:Employee):
    for index,emp in enumerate(employees):
        if emp["emp_id"] == emp_id:
            employees[index] = updated_employee.model_dump()
            return {"message": "Employee updated successfully", "updated_data":updated_employee}
    return {"message": "Employee not found"}


# Delete
@app.delete("/delete-employee/{emp_id}")
def delete_employee(emp_id:int):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            employees.remove(emp)
            return {"message": "employee removed successfully"}
    return {"message": "Employee not found"}
