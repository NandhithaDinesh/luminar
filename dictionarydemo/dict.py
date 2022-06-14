car={"name":"swift","color":"grey","make":"2015","brand":"maruthi","fuel":"petrol","price":"9la","num_airbags":1}
print(car["brand"])
print(car["fuel"])
print(car["price"])
print("transmission_type" in car)
car["transmisson_type"]="manuel"
print(car)
print(car["num_airbags"])
car["num_airbags"]=2
print(car)
print("break_type" in car)
car["break_type"]="abs"
print(car)