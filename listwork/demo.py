# names=["c","c++","python","ruby","java"]
# for i in range(0,len(names)):
#     print(names[i])
# for name in names:
#     print(name)
#.........................................
# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num%2==0:
#         print(num)
#..........................................
# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num>15:
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     elif num==15:
#         print(num)
#................................................
# count=0
# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num>=14 and num<=18:
#         count+=1
# print(count)
#
#
# count=0
# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num in range(14,19):
#         count += 1
# print(count)
# ...............................................
# i=0
# j=0
# k=0
# numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
# for num in numbers:
#     if num>0:
#         i+=1
#     elif num<0:
#         j+=1
#     elif num==0:
#         k+=1
# print(f"positive count={i},negative count={j},zero count={k}")
#  ....................................................................
# sum=0
# numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
# for num in numbers:
#     sum=sum+num
# print("sum=",sum)
# ...............................................................
i=0
j=0
p_sum=0
n_sum=0
numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
for num in numbers:
    if num>0:
        p_sum=p_sum+num
    elif num<0:
        n_sum=n_sum+num
print(f"positive sum={p_sum} negative sum={n_sum}")


