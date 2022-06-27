class Course:
    c_name:str
    c_id:int
    c_fee:int
    def __init__(self,**kwargs):
        self.c_name=kwargs.get("c_name")
        self.c_id = kwargs.get("c_id")
        self.c_fee = kwargs.get("c_fee")
    def print_details(self):
        print(self.c_name,self.c_id,self.c_fee)

cr=Course(c_name="MCA",c_id=10,c_fee=50000)
cr.print_details()
