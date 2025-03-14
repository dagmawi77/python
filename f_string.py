price = 100
print(f"the price is {price:.2f} so please pay")
print(f"the price is {price:.2f}  and the vat amount is {price*0.15:.3f}")

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
print(f"It is very {'expensive' if price>50 else'Chep'}")

fname = input("Enter your name ")
print(f"Your name is {fname.capitalize()}")

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
