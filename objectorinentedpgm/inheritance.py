# .......single inheritance...................................
# class Parent:
#     def phone(self):
#         print("nokia 6.1 plus")
#     def bike(self):
#         print("passion pro")
# class Child(Parent):
#     pass
# ch=Child()
# ch.phone()
# ch.bike()
#...............multilevel inheritance...........................
# class P1:
#     def m1(self):
#         print("inside m1")
# class P2(P1):
#     def m2(self):
#         print("inside m2")
# class P3(P2):
#     def m3(self):
#         print("inside m3")
#
# P3=P3()
# P3.m3()
# P3.m2()
# P3.m1()

# ......mulptiple inheritance...............................
class P1:
    def m1(self):
        print("inside m1")
class P2:
    def m2(self):
        print("inside m2")
class P3(P1,P2):
    def m3(self):
        print("inside m3")

P3=P3()
P3.m3()
P3.m2()
P3.m1()
