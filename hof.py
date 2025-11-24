def fun1():
    print("inside fun 1")
def fun2(ref):
    print("entering fun 2")
    ref()
    print("leaving fun 2")
fun1()
fun2(fun1)