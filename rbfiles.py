ptr=open("car.jpg","rb")
res=ptr.read(6000)
print(res)
ptr.close()
ptr1=open("newcar.jpg","wb")
ptr1.write(res)
ptr1.close()




























