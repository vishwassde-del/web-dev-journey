def outer():
    print("hello")
    def inner():
        print("world")
    return inner
def outsider():
    print("hello hello !!")
res=outer()
res()

