set1={1,2,4,5,6,7,5,6,7}
print(type(set1))
print(set1)
ls=[1,23,4,5,7,7,8]
set2 = set(ls)
print(set2)
print(list(set2))


set3={4,5,7,1,8}
print(set3)
set3.add("90")
print(set3)
set3.remove(8)
print(set3)
set3.update([45,34,3423,232])
print(set3)
print("==============================")

a=set("34wr;sfnnfl sn;fms;mvs;")
b=set("srnsfognsognfsngfsngfsfngsns")
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)