import os
folder = input("enter the folder name:")
os.makedirs(folder, exist_ok=True)
for i in range(1, 4):
    filename = os.path.join(folder, f"file{i}.txt")
    with open(filename, "w") as f:
        f.write(f"this is file {i}.\n")
        f.write("adding line two...\n")
print(f"create 3 files in folder '{folder}'")

