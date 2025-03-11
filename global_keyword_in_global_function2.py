x=400
def myfunc():
    global x
    x = 600
    print(x)

myfunc()
print(x)
