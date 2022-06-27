class Editor:
    def functionalities(self):
        self.funcs=["create new file","execute","save"]
        return self.funcs
class Pycharm(Editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["debug","version controling"])
        return funcs
class Vscode(Editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("more extension support")
        return funcs
vsc=Vscode()
print(vsc.functionalities())
pyc=Pycharm()
print(pyc.functionalities())