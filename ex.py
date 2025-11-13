class Student:
    def __init__(self):
        self.__name="abc"
        self.__age=20
        self.__marks=100
    def setname(self,name):
        if name!=0:
            self.__name=name
    def setage(self,age):
        if age!=0:
            self.__age=age
    def setmarks(self,marks):
        if marks!=0:
            self.__marks=marks
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def getmarks(self):
        return self.__marks
s=Student()
s.setname("xyz")
print(s.getname())
s.setage(22)
print(s.getage())
s.setmarks(77)
print(s.getmarks())