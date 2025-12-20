from itertools import zip_longest

name=["virat","dhoni","gayle","rohit"]
j_num=[18,7,333,45]
country=["ind","ind"]
team=["rcb","csk"]
res=list(zip_longest(name,j_num,country,team,fillvalue="#"))
print(res)
