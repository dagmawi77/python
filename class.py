class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = Person("dagmawi",29)

print(f"his name is {p1.name} and his age is {p1.age}")

#Create Class 
class Person1:
  #self is instance of the class
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
     return f"His name is {self.name} and His age is {self.age}"
  def myfunc(self):
      print("Hello my name is " + self.name)


oneperson = Person1("dagmawi",30)
oneperson.age=33

oneperson.myfunc()

print(oneperson)
del oneperson.age


  
