from fastapi import FastAPI, Path
from typing import Optional 
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"john",
        "age":17,
        "year":"year 12"

    }  
}


@app.get("/")
def index():
    return{"name":"First_Name"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="the id of the student you want to view",gt=0)):
        return students[student_id]


#gt - gretter then 
#ls - less then 
#ge -  gretter or equel 
#le - less or equel 

class student(BaseModel):
    name:str
    age:int
    year : str 

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student in students:
        if (students[student]["name"]==name):
            return students[student]
    return {"Data":"Not Found"}

@app.post("/creat-student/{student_id}")
def creat_student(student_id : int, student: student):
    if (student_id in students):
        return{"error":"student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return{"ERROR": "student isn't exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id]

@app.delete("/delete-student/{studen_id}")
def delte_student(student_id: int):
    if student_id not in students:
        return{"error":"not exist"}
    
    del students[student_id]
    return{"message":"student delte succeful"}



        