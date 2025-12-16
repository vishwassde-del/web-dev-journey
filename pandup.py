import pickle
class emp:
    def __init__(self):
        self.l=[1,2,3,4,5]
e=emp()
f=open("abcd.txt","wb")
pickle.dump(e,f)
f.close()
g=open("abcd.txt","rb")
o=pickle.load(g)
print(o.l)

