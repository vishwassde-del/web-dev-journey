def fun1():
    print("inside fun 1")
def fun2():
    print("inside fun 2")
print(fun1)
print(fun2)
ptr1=fun1
ptr2=fun2
ptr1()
ptr2()