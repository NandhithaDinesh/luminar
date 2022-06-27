class Bottle:
    material:str
    capsity:str
    price:int
    color:str
    def __init__(self,**kwargs):
        self.material=kwargs.get("material")
        self.capasity = kwargs.get("capasity")
        self.price = kwargs.get("price")
        self.color = kwargs.get("color")
    def open(self):
        print("open")
    def print_details(self):
        print(self.price,self.material)

bt=Bottle(material="plastic",capasity="800ml",price=159,color="transparant")
bt.open()
bt.print_details()
