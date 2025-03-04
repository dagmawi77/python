a = 1000
b = 300
c = 100

if a < b:
    print("b is greatr than a")
elif a == b:
    print("b and a is equal")
else:
    print("a is greater than b")

if a > b : print("a is greate than b")

print(f"A={a}") if (a>b) else print(f"B={b}")
print("A") if a > b else print("=") if a == b else print("B")

# using Ternary Operators

if a>b and b>c:
    print ("A is Greater From All Value")
elif not b > a or b<c:
    print("B is the middle value")
else:
    print("C is the smallest Value") 
