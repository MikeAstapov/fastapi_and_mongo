from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, Field, EmailStr
from pymongo import MongoClient

app = FastAPI()
connection_url = f"fastapimongo-mongodb-1:27017"
print(f"Connecting to: {connection_url}")
client = MongoClient(connection_url)
db = client['fastapidb']
collection = db['students']


class Student(BaseModel):
    id: int
    name: str = Field(...)
    surname: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    GPA: float = Field(le=5.0)


class UpdateStudents(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    GPA: Optional[float]


@app.get('/')
def say_hello():
    return "Hello from docker-compose"


@app.post('/', response_description="Add new student", response_model=Student)
async def create_student(student: Student = Body(...)):
    student = jsonable_encoder(student)
    new_student = collection.insert_one(student)
    created_student = collection.find_one({"id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@app.get('/users/', response_description="Check all students", response_model=List[Student])
def get_students():
    students = collection.find()
    if students:
        return students
    raise HTTPException(status_code=404, detail="DB is empty")


@app.get('/{id}', response_description="Check one student", response_model=Student)
def get_student(id: int):
    if (student := collection.find_one({"id": id})) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.put("/{id}", response_description="Update a student", response_model=Student)
def update_student(id: int, student: UpdateStudents = Body(...)):
    student = {k: v for k, v in student.model_dump().items() if v is not None}

    if len(student) >= 1:
        update_result = collection.update_one({"id": id}, {"$set": student})

        if update_result.modified_count == 1:
            if (updated_student := collection.find_one({"id": id})
            ) is not None:
                return updated_student

    if (existing_student := collection.find_one({"id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.delete("/{id}", response_description="Delete a student")
def delete_student(id: int):
    delete_result = collection.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_200_OK, content=f"Student {id} deleted successfully.")

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", reload=True, log_level='info')