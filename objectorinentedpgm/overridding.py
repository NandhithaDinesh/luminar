# class Parent:
#     def phone(self):
#         print("nokia")
#     def bike(self):
#         print("passion pro")
# class Child(Parent):
#     def phone(self):
#         print("iphone")
#     def bike(self):
#         print("duke")
# ch=Child()
# ch.phone()
# ch.bike()

# ........................................................

class Parent:
    def properties(self):
        self.props={"mobile":"nokia","bike":"passionpro"}
        return self.props
class Child(Parent):
    def properties(self):
        props=super().properties()
        props["car"]="swift"
        return props
ch=Child()
print(ch.properties())

