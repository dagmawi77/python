vegitable = ['potato', 'tomato', 'onion', 'carrot', 'cucumber']
ovegitable=[]

for x in vegitable:
    if "o" in x:
        ovegitable.append(x)

print(vegitable)
print(ovegitable)

newlist=[x for x in vegitable if "c" in x]
print(newlist)