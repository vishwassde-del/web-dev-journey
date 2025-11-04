import copy
l=["a","b","c",[10,20,30]]
l1=copy.deepcopy(l)
print(l,l1)
l[3][2]=300
print(l,l1)
