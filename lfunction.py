l=lambda a,b:a+b
print(l(5,5))
#nested function:
def fun1():
    print("inside outer")
    def fun2():
        print("inside inner")
    fun2()
fun1()
#global variables
a=10
def f1():
    b=20
    print(a,b)
def f2():
    a=100
    b=200
    print(a, b)
f1()
f2()
