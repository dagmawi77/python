x = "Awsome"
def myfunc():
    x = "Fantastic"
    print("Python is " + x)

myfunc()  # Python is Fantastic
print("Python is " + x)  # Python is Awsome
# Explanation: The x variable inside the function is a local variable. The function will print the local x, but the global x will remain the same.