f = open("myfile.txt","x")
f.close()

f = open("myfile.txt","a")
f.write("\n This is new text")
f.close()

f = open("myfile.txt","r")
print(f.read())
