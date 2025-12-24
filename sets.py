a1={1,2,3,4,5,6,7,8}
print(a1)
a2={1,2,3,1,2,3}
print(a2)
print(type(a2))
a3={}
print(type(a3))
#adding and deleting
a=set()
for i in range(5):
    a.add(i)
print(a)
a.update([5,6,7,8])
print(a)
a.discard(7)
print(a)
s={10,20,30,40}
print(s)
for i, j in enumerate(s):
    print(i,j)