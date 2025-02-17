# quition inside qution
print("I said: 'I am a programmer'")
print('I and "Dagmqawi"')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[4])

# Looping Through a String
for x in "banana":
    print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")
else:
    print("No, 'free' is not present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")
else:
    print("No, 'expensive' is present.")

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])
# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
a = "Hello, World!"
print(a.upper())
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# String Methods
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
print(a.strip())  # returns "Hello, World!"
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))
print(len(a))
print(a[1])

