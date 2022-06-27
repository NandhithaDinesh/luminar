class Student:
    name:str
    roll_no:int
    course:str
    def set_student(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
    def print_student(self):
        print(self.name,self.roll_no,self.course)

p1=Student()
p2=Student()
p1.set_student("nandhitha",100,"mca")
p1.print_student()