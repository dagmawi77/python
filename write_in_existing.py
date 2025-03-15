f = open("test.txt","a")
f.write(" \n new line add ")
f.close()

f = open("test.txt","r")
print(f.read())