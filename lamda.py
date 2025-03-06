x = lambda a : a+10
print(x(5))

x =lambda a,b : a*b
print(x(5,6))

x = lambda a,b,c : a+b+c
print(x(10,20,30))

def myfunc(n):
    return lambda a:a*n

result = myfunc(10)
print(result(5))

mytripler = myfunc(3)
print(mytripler(11))
