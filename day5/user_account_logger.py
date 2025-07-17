user = input("username: ")
with open("users.txt", "a") as f:
    f.write(user + "\n")
