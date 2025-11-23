def outer():
    a,b=10,20
    print(a,b,"*******        non local            *******")
    def inner():
        nonlocal a
        a,b=100,200
        print(a,b,"********           local          *******")

    print(a)
    inner()
    print(a)
outer()

