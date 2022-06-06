flag=0
arr=[1,2,3,13,14,15,16,65,78,89]
element=14
for num in arr:
    if num==element:
        flag=1
        break
if flag==1:
    print("element found")
else:
    print("not found")
