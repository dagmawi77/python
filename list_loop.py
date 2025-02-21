mylist =["Laptop","Desktop","Tablet","Smartphone","Smartwatch","SmartTV"]

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

y=0
while y < len(mylist):
    print(mylist[y])
    y+=1

# List Comprehension
[print(x) for x in mylist]