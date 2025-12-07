l1=[10,20,30]
l2=[40,50,60]
print(l1+l2)
print(l1*2)
l=[1,2,3,4,5,6,7,8,9]
print(l[-2:-6:-1])
print(len(l))
print(l[::-1])
print((l[::2]))
print(l[7:3])
print(min(l))
print(max(l))
print(any(l))#min 1 value is non-zero
print(all(l))#all values are non-zero
l=[0,0,0,"abc"]
print(any(l))#(string too)
print(all(l))#(string too)
l=[1,2,3,4,5,6,7,8,9]
for i,j in enumerate(l):
    print(i,j)