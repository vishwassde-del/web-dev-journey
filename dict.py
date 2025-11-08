e={"name":"abc","age":"18","sal":"100"}
print(e)
e["new"]=20
print(e)
for i in e:
    print(i)
for i in e.keys():
    print(i)
for i in e.values():
    print(i)
for i in e.items():
    print(i)
#nested dictionary
student={
    "name":"abc",
    "age":18,
    "pnum":{"mob":9999,
            "tel":6666},
    "addr":{"resi":"pqr",
            "perm":"xyz"}
}
print(student)
print(student["name"])
print(student["pnum"]["mob"])
print(student["addr"]["perm"])
