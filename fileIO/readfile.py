# f=open("abc.txt","r")
# for line in f:
#     print(line)
# f=open("abc.txt")
# out=[line.rstrip("\n") for line in f]
# print(out)
#....................................
# f=open("abc.txt","w")
# lst=["python","javascript","c#"]
# company_name="luminar"
# for lan in lst:
#     lan+="\n"
#     f.write(lan)
#..........................................
# f.write(company_name)
#........................................



students=open("students.txt")
all_students=[stud.rstrip("\n") for stud in students]
f_students=open("failed.txt")
failed_students=[stud.rstrip("\n") for stud in f_students]
passed=open("passed.txt","w")
passed_students=set(all_students)-set(failed_students)
print(passed_students)
for st in passed_students:
    st+="\n"
    passed.write(st)

# to append a new name to the file
name="arya"
fp=open("passed.txt","a")
fp.write(name)


