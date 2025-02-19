print (200>90)
print (200<90)
print (200==90)

a=200
b=90
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))
print(bool(0.0))
print(bool(""))
print(bool(False))
print(bool(0j))
print(bool(0.0))

class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj))
print(bool(myobj.__len__()))

def myFunction():
    return True
print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

x=500

print(isinstance(x,int))


