mylist = ["shiro","Tibis","Kitfo","Doro",1,34,[1,2,5],(1,2,5),{1,2,5},{1:2,5:6},True]
print(mylist)
print(mylist[1])
print(len(mylist))
print(mylist[-1])
print(mylist[-2])
print(mylist[2:5])
print(mylist[:4])
print(mylist[4:])

if "shiro" in mylist:
    print("Yes, 'shiro' is in the list")

mylist[-1]=False
print(mylist)
mylist[1:3]=["Dulete","Firfir"]
print(mylist)
mylist[1:2]=["dabo fifir","Gomen Besiga","Gomen Tibs"]
print(mylist)
print(len(mylist))
mylist[1:3]=["Kitfo"]
print(mylist)
print(len(mylist))
mylist.insert(1,"Dabo")
print(mylist)
print(len(mylist))

# Add List
mylist.append("Gomen")
print(mylist)
mysecondlist=["Gomen","Gomen Tibs","Gomen Besiga"]
mylist.extend(mysecondlist)
print(mylist)
thisistuple=("Gomen","Gomen Tibs","Gomen Besiga")
mylist.extend(thisistuple)
print(mylist)