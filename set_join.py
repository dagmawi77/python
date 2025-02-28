set1 = {"set1","set2","set3"}
set2 = {1,2,3,4}
set3 = set1.union(set2)
print(set3)
set4 = set2 | set3
print(set4)
set5 = set1.union(set2,set3,set4)
print(set5)
set6 = set1 | set2 | set3 | set4 | set5
print(set6)
thisislist=["a","b","c"]
thisistuple=("tuple1","tuple2","tuple3")
set7 = set6.union(thisislist,thisistuple)
print(set7)
set8={6,8,9,0}

set8.update(set7)
print(set8)

set9 = set8.intersection(set7)
print(set9)
set10 = set8 & set7
print(set10)

set11=set8.difference(set7)
print(set11)
set12=set8-set7
print(set12)