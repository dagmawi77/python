#decalring tuple
thisistuple=("tuple1","tuple2","tuple3")

y=list(thisistuple)

y[0]="come from list"

thisistuple=tuple(y)

print(thisistuple)

y =list(thisistuple)
y.append("add intuple")
thisistuple=tuple(y)

print(thisistuple)

x=("newtupe",)

thisistuple+=x
print(thisistuple)

y=list(thisistuple)
y.remove("add intuple")
thisistuple=tuple(y)
print(thisistuple)