# for i in range(0,10):
#     print(i)
# for i in range(0,50,5):
#     print(i,end=" ")
# numbers=range(10,100)
# for i in numbers:
#     print(i,end=" ")
# numbers=range(10,0,-1)
# for i in numbers:
#     print(i,end=" ")
# for i in range(1,50):
#     if i==25:
#         break
#     print(i)
# for i in range(1,50):
#     if i==25:
#         continue
#     print(i)
# num=7
# flag=0
# for i in range(2,num):
#     if(num%1==0):
#         flag=1
#         break
# if flag==0:
#     print("prime")
# else:
#     print("not prime")
#.........highest common factor of 15 and 35.....
# num1=15
# num2=35
# hcf=1
# limit=num1 if num1<num2 else num2 #to find the minimum of num1 and num2
# for i in range(2,(limit+1)):
#     if num1%i==0 and num2%i==0:
#         hcf=i
# print(hcf)
#.........highest common factor of 3 numbers......
# num1=15
# num2=35
# num3=45
# hcf=1
# limit=0
# if(num1<num2) and (num1<num3):
#     limit=num1
# elif(num2<num1) and (num2<num3):
#     limit=num2
# elif(num3<num1) and (num3<num1):
#     limit=num3
# for i in range(2,(limit+1)):
#      if num1%i==0 and num2%i==0 and num3%i==0:
#         hcf=i
# print(hcf)
#............pattern printing......

# for row in range(1,5):
#     for col in range(1,5):
#         print(col,end=" ")
#     print()

#...........................
# for i in range(1,5):
#     for j in range(1,3):
#         print(i,end=" ")
#     print()
#...........................
# for row in range(1,5):
#     for col in range(1,5):
#         if(row>=col):
#             print(col,end=" ")
#     print()

# for row in range(1,5):
#     for col in range(1,row+1):
#             print(col,end=" ")
#     print()
# for row in range(1,5):
#     for col in range(1,row+1):
#             print(row,end=" ")
#     print()
#
# for row in range(1,5):
#     for col in range(1,row+1):
#             print("#",end=" ")
#     print()
# for row in range(1,5):
#     for col in range(5,row,-1):
#             print("#",end=" ")
#     print()
#.......full pyramid......

# for row in range (1,5):
#     for space in range(1,(5-row)):
#         print(" ", end=" ")
#         for col in range(1,(row+1)):
#            print("* ",end=" ")
#     print()
#..............................
for row in range (1,5):
    for col in range(1,7):
        if row==4 or (col+row==4)or(col-row==2):
            print("*",end="")
        print()





