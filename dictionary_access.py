thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("year")
print(x)
x= thisdict.keys()
print(x)

thisdict["color"]="white"
print(x)

x = thisdict.values()

print(x)

thisdict["year"]=2000

print(x)

thisdict["color"]="red"
print(x)

x = thisdict.items()

print(x)

thisdict["year"]=20005
print(x)

if "model" in thisdict:
    print("Yes The model is present in Dectionary")

thisdict.update({"year":2005})

print(x)

# add Iteams In dictionary
#first Method 

thisdict["price"]=3000000.00
print(x)

thisdict.update({"engine type":"V8"})
print(x)
