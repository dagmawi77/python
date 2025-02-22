firute = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
firute.sort()
print(firute)

randomnubers = [11,55,44,33,22,66,99,88,77]
randomnubers.sort()
print(randomnubers)

firute.sort(reverse=True)
print(firute)
randomnubers.sort(reverse=True)
print(randomnubers)

def myfunc(x):
    return abs(x-50)

randomnubers.sort(key=myfunc)
print(randomnubers)

insensitive = ["banana", "Orange", "Kiwi", "cherry"]

insensitive.sort()
print(insensitive)
insensitive.reverse()
print(insensitive)

insensitive.sort(key=str.lower)
print(insensitive)