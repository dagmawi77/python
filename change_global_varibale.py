x = "Awsome"
def myfunc():
    global x
    x = "Fantastic"
    print("Python is " + x)

myfunc()  # Python is Fantastic
print("Python is " + x)  # Python is Fantastic
# Explanation: If you use the global keyword, the variable belongs to the global scope.