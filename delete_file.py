import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("The file Sucessfully Deleted")
else:
    print("The file is not Exist")