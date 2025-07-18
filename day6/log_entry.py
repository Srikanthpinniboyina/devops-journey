import os
from datetime import datetime
folder = input("enter folder name")
log_file = os.path.join(folder, "app.log")
os.makedirs(folder, exist_ok=True)
if os.path.exists(folder):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open(log_file, "w") as f:

        f.write(f"current time:{current_time}\n")
    with open(log_file, "a") as f:
        f.write("log entry\n")
else:
    print("error occure")
