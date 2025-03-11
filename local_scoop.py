def myfunc():
    x=100
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()