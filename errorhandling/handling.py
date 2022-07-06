
# try.................
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# try:
#     res=num1/num2
#     # print(f"resutlt={res}")
# except Exception as e:
#     # print(e)
#     num2=int(input("enter second number"))
#     print(num1/num2)
# finally:
#
#     print("database transaction")
#     print("file handling")

# raise.................
age=int(input("enter num1"))
if(age<18):
    raise Exception("not eligible for taking booster dose")
else:
    print("eligible")
phone=input("enter phone number")
if(len(phone)!=10):
    raise Exception("invalid phone number")
else:
    print("valid")
# try: doubtful code
# except: handling code
# finally: clean up process
# raisingkey throwing custom exception

