class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x= self.a 
        self.a *=2
        return x

mynumberobj = MyNumber()
myiter = iter(mynumberobj)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))