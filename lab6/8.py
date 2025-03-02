import os


def existance(path):
    return os.path.exists(path)

x = existance("qeinw0g")

if x == True:
    print(f"pos: {os.path.dirname(x)} \n")
    print(f"port: {os.path.basename(x)}")
else:
    print("does not exist")