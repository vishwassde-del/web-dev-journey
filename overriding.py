class A:
    def disp(self):
        print("inside a")
class B(A):
    def disp(self):
        print("inside b")
class C(B):
    def disp(self):
        print("inside c")
c=C()
c.disp()
c.disp()
c.disp()
