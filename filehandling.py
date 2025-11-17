"""name=input("enter a name : ")
ptr=open("abcd.txt","w")
ptr.write(name)
ptr.close()"""
# str1=open("abcd.txt")
# print(str1.readlines())
# str1.close()
# name=input("enter a name : ")
# ptr=open("abcd.txt","a")
# ptr.write(name)
# ptr.close()

#tell seek

ptr=open("abcd.txt",'r')
pos=ptr.tell()
print(pos)
res=ptr.read(5)
print(res)
print(ptr.seek(2))
print(ptr.tell())