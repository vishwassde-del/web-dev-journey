l=[]
i=0
while i<5:
    num=int(input(f"enter no. {i+1} : "))
    l.insert(i,num)
    i+=1
print("list is : ",l)
def even(n):
    if n%2==0:
        print(n)
    else:
        pass
i=0
print("filtered elements are :")
while i<5:
    even(l[i])
    i+=1

