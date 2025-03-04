i = 1
while i < 6:
    print(f"the I number {i}")
    i += 1
 
# Break

i = 1
while i<6:
    print(f"the I number {i}")

    if i ==3:
        break
    i+=1

# Continue

i = 1
while i<6:
    i+=1
    if i ==3:
        continue
    print(f"the I number {i}")