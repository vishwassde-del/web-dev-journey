from copy import deepcopy
a={"name":"abc",
   "age":20}
b=a
c=a.copy()
b["age"]=30
print(a)
print(b)
print(c)