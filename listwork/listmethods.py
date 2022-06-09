# lst=[10,11,12,14,15,16,17,12,12,12,12,100]
# evenlist=[]
# for num in lst:
#     if num%2==0:
#         evenlist.append(num)
# print(evenlist)
# evenlist.sort(reverse=True)
# print(evenlist)
# print(lst.count(12))

#...............................................
# lst1=[10,11,12,13,14]
# lst2=[11,14,15,16,17]
# duplicate_lst=list()
# for num in lst1:
#     if num in lst2:
#         duplicate_lst.append(num)
# print(duplicate_lst)
#..................................................
lst1=[10,11,11,12,13,14,14,14]
dup_list=[]
for i in range(0,len(lst1)):
    for j in range((i+1),len(lst1)):
        if lst1[i]==lst1[j]:
            dup_list.append(lst1[i])
print(dup_list)
