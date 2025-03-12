import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)

#convert python to json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y= json.dumps(x)

print(y)


print(json.dumps(True))

print(json.dumps([1,2,4,5,5,6]))
print(json.dumps(4.8))
#print(json.dumps({536,37,73,36}))
print(json.dumps("Hello Json"))
print(json.dumps(("apple", "bananas")))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
y= json.dumps(x , indent=4)
print(y)

json.dumps(x, indent=4, separators=(". ", " = "))

json.dumps(x, indent=4, sort_keys=True)






