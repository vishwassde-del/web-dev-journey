s=input("enter a string :")
rev=""
for i in s:
    rev=i+rev
if rev==s:
    print("pallindrome")
else:
    print("not a pallindrome")