id=["101","102","103","104"]
names=["abc","bcd","cdf","dfe"]
res1=dict(zip(id,names))
print(res1)
mob=["12","34","56","78"]
adr=["a","b","c","d"]
#if we want to add multiple lists for a dict . convert all other lists into a single list:::::::::
data=list(zip(names,mob,adr))
res3=dict(zip(id,data))
print(res3)

#wrong way
#   res2=dict(zip(id,names,mob,adr))   print(res2)


