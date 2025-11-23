a=10
def fun1():
    global a
    a,b=100,200
    print(a,b)
def fun2():
    global a
    a,b=150,250
    print(a,b)
print(a)
fun1()
print(a)
fun2()
print(a)

