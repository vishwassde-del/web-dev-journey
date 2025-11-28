#list is dynamic
l=[]
i=0
while True:
    n=int(input("enter a number :"))
    l.insert(i,n)
    i+=1
    c=int(input("do you want to continue :\n 1.yes 2.no :"))
    if c==1:
        continue
    else:
        break
print(l)