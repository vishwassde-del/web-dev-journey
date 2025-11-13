try:
    a=int(input("enter a no. a:"))
    b=int(input("enter a no. b:"))
    print(a/b)
except Exception as e :
    print("error occured")
    print(e)