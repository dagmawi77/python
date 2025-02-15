def myfunc():
    global x
    x = "Fantastic"
    print("Python is " + x)
myfunc()  # Python is Fantastic
print("Python is " + x)  # Python is Fantastic
# Explanation: If you use the global keyword, the variable belongs to the global scope.
# Also, there is a way to change the value of a global variable inside a function.
# To do this, use the global keyword.