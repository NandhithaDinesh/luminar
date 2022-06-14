# st={1,3,"yes",True,10.6}
# print(st)
# #........................................
# lst=[6,4,11,11,12,13,16,16,16]
# st=set(lst)
# print(st)

st1={1,6,8,9,5}
st2={9,7,8,4}
# st1.add(10)
# print(st1)

union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

diff_set=st1.difference(st2)
print(diff_set)

students=["ram","ravi","hari","tom","niki","jain","jhon"]
passed_students=["ravi","hari","tom"]
failed_student=set(students).difference(set(passed_students))
print(failed_student)