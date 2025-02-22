myfirtslist=["abebe","kebe","bekele"]
mysecondlist=["lema","jemale","abdela"]

newlist = myfirtslist + mysecondlist

print(newlist)

for x in myfirtslist:
    mysecondlist.append(x)

print(mysecondlist)

mysecondlist.extend(myfirtslist)

print(mysecondlist)
