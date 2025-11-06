class brain:
    def __init__(self,status):
        self.bstatus=status
    def getbrain(self):
        print("brain is working")
class car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("car is moving")
class person:
    def __init__(self):
        self.pname="vishwas"
        self.b1=brain("active")
        self.c=""
    def hascar(self,p):
        self.c=p
p1=person()
c1=car("audi")
print(p1.pname)
print(p1.b1.bstatus)
p1.b1.getbrain()
p1.hascar(c1)
print(p1.c.cname)
p1.c.getcar()
print("*************************after deleting the main object*******************************")
del p1
print(c1.cname)
c1.getcar()
print(p1.b1.bstatus)


