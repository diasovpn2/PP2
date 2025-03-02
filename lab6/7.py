import os


def access(path):
    x = os.path.exists(path)
    y = os.access(path, os.R_OK)
    z = os.access(path, os.W_OK)
    c = os.access(path, os.X_OK)
    return print(f" exists {x} \n readable {y} \n writable {z} \n executable {c}")

access("rype")