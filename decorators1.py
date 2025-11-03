def main():
    str="abcd"
    return str
def outer(ptr):
    print("inside outer")
    main()
    def inner():
        print("entering inner")
        str=ptr()
        print(str.upper())
        print("leaving inner")
    return inner
res=outer(main)
res()

