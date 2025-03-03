thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
thisdict["price"]=3000000.00
print(x)

thisdict.update({"engine type":"V8"})
print(x)

for y in thisdict:
    print(y) 
    print(thisdict[y])
for m in thisdict.values():
    print(m)

for k in thisdict.keys():
    print(k)

for x,y in thisdict.items():
    print(x,y)