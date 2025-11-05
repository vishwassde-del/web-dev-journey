import copy
from copy import deepcopy
a={"name":"abc",
   "age":20,
   "bf":{"name1":"pqr",
         "name2":"xyz"}
}
b=a.copy()#deep 1D dict
c=copy.deepcopy(a)#deep copy for nested dict
print(a)
print(b)
print(c)
a["bf"]["name3"]="hij"
print(a)
print(b)#will affect because deep 1D dict
print(c)#deep copy archived for nested dict