class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"The First name is {self.fname} and last name is {self.lname}"
class Student(Person):
    def __init__(self, fname, lname,year):
        self.year=year
        #super().__init__(fname, lname)
        Person.__init__(self,fname,lname)
    def __str__(self):
        return f"Ths student name is {self.fname} {self.lname} and is graduation year is {self.year}"

student1= Student("dagmawi","letarik",2017)
print(student1)

