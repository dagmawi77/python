mylist=[1,5,6,7]
# adding On existing list at the end of the list
mylist.append(["Extended",80,200])
print(mylist)
#removing all Iteams from List 
mylist.clear()
print(mylist)

newone=[100,500,78,90]

newtwo=newone.copy()

print(newtwo)
namelist = ["abebe","lema","bekele"]

x=newtwo.count(90)
print(x)

namelist.extend(newone)

print(namelist)

y=namelist.index("abebe")

print(y)

namelist.insert(5,"kebede")
print(namelist)

namelist.pop(7)
print(namelist)
namelist.remove(500)
print(namelist)

namelist.reverse()

print(namelist)
newlist =["a","x","y","c"]

newlist.sort(reverse=True)

print(newlist)
