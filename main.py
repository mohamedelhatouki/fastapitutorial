from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # يسمح بالاتصال من أي موقع
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id:int
    name: str
    grade: float
students=[
    Student(id=1,name='simo',grade=17.9),
    Student(id=2,name='ahmed',grade=10),

]

  
@app.get("/students/")
def get_students():
    # إرجاع البيانات بناءً على الهيكل المحدد
    return students
@app.post("/students/")
def create_student(new_student:Student):
    students.append(new_student)
    return new_student
@app.put("/students/{student_id}")
def update_student(student_id:int ,updated_student:Student):
    for index,student in enumerate(students):
        if student.id==student_id:
            students[index]=updated_student
            return updated_student
    return {"error":"student not found"}
@app.delete("/students/{student_id}")
def delate_student(student_id:int ):
    for index,student in enumerate(students):
        if student.id==student_id:
            del students[index]
            return{"massage":"student delated"}
    return {"error":"student not found"}


    

