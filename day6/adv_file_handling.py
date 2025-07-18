import os
filename = "file1.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print("File contents:", f.read())
    with open(filename, "a") as f:
        f.write("\nNew line added")
else:
    print("File does not exist")
