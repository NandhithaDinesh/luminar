mobile={
    "mobile_name":"redmi",
    "display":"led",
    "price":45000,
    "ram":"6gb",
    "memory":"64gb"

}
print(mobile.get("mobile_name"))
print(mobile.get("display"))
print(mobile.get("ram"))

if "band" in mobile:
    mobile["band"]="5g"
else:
    mobile["band"]="4g"
print(mobile)

mobile["band"]="5g" if "band" in mobile else "4g"
print(mobile)

if mobile["price"]>40000:
    mobile["price"]-=1000
else:
    mobile["price"]-=500

print(mobile)
