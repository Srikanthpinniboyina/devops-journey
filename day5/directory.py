import os
folder = input("enter directory name")
os.makedirs(folder, exist_ok=True)
for i in range(3):

    with open(f"{folder}/file(i+1).txt", "w") as f:
        f.write("test file")
