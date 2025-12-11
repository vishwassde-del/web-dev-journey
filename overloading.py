class A:
    def disp(self,a,b,c):
        print("inside a")
class B(A):
    def disp(self,a,b):
        print("inside b")
class C(B):
    def disp(self,a):
        print("inside c")
c=C()
c.disp(10,20,30)
c.disp(10,20)
c.disp(10)
