import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} deleted successfully.")
        else:
            print(f"Cannot delete {path}.")
    else:
        print(f"{path} does not exist.")


delete_file("file_to_delete.txt")