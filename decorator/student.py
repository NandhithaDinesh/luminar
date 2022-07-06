class Course:
    course_name:str
    active_status:bool

    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")
    def __str__(self):
        return self.course_name


class Batch:
    course: Course
    batch_code: str
    start_date:str

    def add_batch(self, **kwargs):
        self.course = kwargs.get("course")
        self.batch_code = kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code


class Student:
    student_name:str
    gender: str
    rol: str
    batch:Batch

    def add_student(self, **kwargs):
        self.student_name = kwargs.get("student_name")
        self.gender = kwargs.get("gender")
        self.rol = kwargs.get("rol")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name

django=Course()
django.add_course(course_name="django",active_status=True)
bigdata=Course()
bigdata.add_course(course_name="bigdata",active_status=True)
db1=Batch()
db1.add_batch(course=django,batch_code="djmay2k22",start_date="5-6-2022")
bd1=Batch()
bd1.add_batch(course=bigdata,batch_code="bdmay2k22",start_date="5-6-2022")
rahul=Student()
rahul.add_student(student_name="rahul",gender="male",rol="123",batch=db1)
akshay=Student()
akshay.add_student(student_name="akshay",gender="male",rol="1124",batch=db1)
amal=Student()
amal.add_student(student_name="amal",gender="male",rol="1237",batch=bd1)
asha=Student()
asha.add_student(student_name="asha",gender="female",rol="1129",batch=bd1)
print(rahul.batch.course.course_name)