def main():
    print("inside main")
def outer(ptr):
    print("inside outer")
    main()
    def inner():
        print("entering inner")
        ptr()
        print("leaving inner")
    return inner
res=outer(main)
res()