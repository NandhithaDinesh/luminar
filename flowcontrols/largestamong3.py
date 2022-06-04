# num1=20
# num2=190
# num3=78
# if (num1>num2) & (num1>num3):
#     print("num1 largest")
# elif (num2>num1) & (num2>num3):
#     print("num2 largest")
# elif (num3>num1) & (num3>num2):
#     print("num3 largest")
# elif (num1==num2) & (num1==num3):
#     print("all are same")
# num1=20
# num2=190
# num3=78
# if (num1>num2) and (num1>num3):
#     )    print("num1 largest")
# elif (num2>num1) and (num2>num3):
#     print("num2 largest")
# elif (num3>num1) and (num3>num2):
#     print("num3 largest")
# elif (num1==num2) and (num1==num3):
#     print("all are same"

#.....second largest among 3...,
num1=20
num2=120
num3=50
if(num1>num2) & (num1>num3):
    if(num2>num3):
        print(f"{num2 } second largest")
    else:
        print(f"{num3} second largest")
elif(num2>num1) & (num2>num3):
    if(num1>num3):
        print(f"{num1} second largest")
    else:
        print(f"{num3} second largest")
elif(num3>num1) & (num3>num2):
    if(num1>num2):
        print(f"{num1} second largest")
    else:
        print(f"{num2} second largest")