l=[]
for i in range(5):
    n=int(input(f"enter {i+1} number : "))
    l.append(n)
def even(n):
    if n%2==0:
        return True
    else:
        return False
res=list(filter(even,l))
print(res)
