print("---------------------")

ls=[5,True,"34343"]
print(ls)
ls.append("找")
print(ls)
ls2=[1,2,3]
ls.extend(ls2)
print(ls)
ls.insert(3,"张龙")
print(ls)

del ls[1]
print(ls)
ls.pop()
print(ls)
ls.pop(4)
print(ls)
ls.remove("张龙")
print("---------------------")
ls2 = [1,25,7,4]
ls2.sort();
print(ls2)
ls2.reverse()
print(ls2)

print(sorted(ls2))

print(len(ls))