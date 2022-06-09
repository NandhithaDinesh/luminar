# lst=[2,3,4,6]
# sum=8
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         curr_sum=lst[i]+lst[j]
#         if curr_sum==sum:
#             print(f"pairs {lst[i]},{lst[j]}")
#             break
#........................................................
lst=[2,3,4,6,8]
element=8
lst.sort()
low=0
upp=len(lst)-1
count=1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==element:
        print(f"pairs{lst[low]},{lst[upp]}")
        break
    elif cur_sum>element:
        upp-=1
    elif cur_sum<element:
        low+=1
