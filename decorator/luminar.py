# class Staff(object):
#     id:int
#     name:str
#     role:str
#     def __init__(self,*args,**kwargs):
#         self.id=kwargs.get("id")
#         self.name = kwargs.get("name")
#         self.role = kwargs.get("role")
#     def __str__(self):
#         return self.name
#
# user=Staff(id=100,name="nandhu",role="admin")
# print(user)





class Employee:
    def __init__(self,**kwargs):

        self.eid=kwargs.get("eid")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")
    def __str__(self):
         return self.name
emp=Employee(eid=12,name="nandhitha",role="admin")

class Department:

    def __init__(self,**kwargs):
        user = kwargs.get("user")
        if user.role=="admin":

            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("no access")
    def __str__(self):
         return self.dept_name
dept=Department(dept_name="hr",user=emp)
print(dept)

