fruits=["banana","mango","apple"]
for x in fruits:
    print(x)

forstring="This is me"

for x in forstring:
    print(x)

for x in range(6):
    #break after print
    print(x)
    if x==4:
        break
for x in range(7):
    if x==4:
        break
    print(x)

for x in range(6):
    #break after print
    print(x)
    if x==4:
        continue
for x in range(7):
    if x==4:
        continue
    print(x)

for x in range(2,8):
    print(x)

for x in range(3,40,4):
    print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
for x in [0, 1, 2]:
  pass