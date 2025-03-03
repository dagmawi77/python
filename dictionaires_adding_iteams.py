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
