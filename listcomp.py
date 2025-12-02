l=[1,2,3,4,5,6]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
print(l1)
l2=[i for i in l if i%2==0]
print(l2)
l3=list(range(5,10))
print(l3)
