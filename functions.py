def add():
    a,b=10,20
    print("npnr")
    print(a+b)
add()
def add1():
    a,b=10,20
    print("npwr")
    return a+b
print(add1())
def add3(a,b):
    print("wpnr")
    print(a+b)
x,y=10,20
add3(x,y)
def add4(a,b):
    print("wpwr")
    return a+b
print(add4(x,y))