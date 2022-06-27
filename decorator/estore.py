class User:
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.role = kwargs.get("role")
class AddProduct:
    def post(self,**kwargs):
        u_ser=kwargs.get("user")
        if u_ser.role=="admin":
            self.product_name=kwargs.get("p_name")
            self.user=kwargs.get("user")
        else:
            print("no privillage")
user=User(name="nandhu",role="customer")
pro1=AddProduct()
pro1.post(p_name="laptop",user=user)
