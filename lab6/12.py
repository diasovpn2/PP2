import shutil

def copy_file(x, y):
    try:
        shutil.copy(x, y)
        print(f"Copied contents from {x} to {y}")
    except FileNotFoundError:
        print(f"Source file '{x}' not found.")

copy_file("x.txt", "y.txt")