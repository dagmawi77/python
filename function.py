def myfunc():
    print("hello Function")
myfunc()

def myfunc(fname,lname):
    print(f"Hell {fname} {lname}")

myfunc("Dagmawi","Letarik")

def myfunction(*kids):
    print(f"the kids {kids[1]}")

myfunction("dagmawi","abele","abebe")

def myfunc(fname,lname):
    print(f"Hell {fname} {lname}")
myfunc(lname="Letarik",fname="Dagmawi")

def myfunction(**kids):

    print("his last name is "+ kids["lname"])

myfunction(fname="abebe",lname="kebede")

def iamfromfunc(contery="Ethiopia"):
    print("I am Form " +contery)

iamfromfunc("Egypt")
iamfromfunc()

#passing list agrument

def listfunc(food):
    for x in food:
        print("The food name is "+x)

namef=["banana","mango","Avocado"]

listfunc(namef)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def myfunction():
  pass

def my_function(x, /):
  print(x)

my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
