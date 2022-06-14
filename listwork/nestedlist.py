lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
# for sub_lst in lst:
#     for num in sub_lst:
#         if num>15:
#             print(num)
#..........................................
# print(lst)
# flatten_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_list.append(num)
# print(max(flatten_list))
#list comprehension
f_list=[num for slist in lst for num in slist]
print(f_list)

num_gt_sixteen=[num for num in f_list if num>16]
print(num_gt_sixteen)

odd_num=[num for num in f_list if num%2!=0]
print(odd_num)

even_sum=[num for num in f_list if num%2==0]
print(sum(even_sum))

even_sum=sum([num for num in f_list if num%2==0])
print(even_sum)

f_list=[num for slist in lst for num in slist]
mapped_list=[num+1 if num>25 else num-1 for num in f_list]
print(mapped_list)


