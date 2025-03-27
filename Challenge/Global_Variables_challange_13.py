"""
Global Variables


Hint


Write a Python function called myfunc. This function should print "Python is awesome" using the global variable x.

Requirements

Function `myfunc` should print the correct message.
"""

x = "awesome"

# Define your function here
def myfunc():
    global x  # Access the global variable
    print("Python is", x)  # Print the message using x

# Your function is called
myfunc()