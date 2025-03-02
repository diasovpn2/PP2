import string

def gen():
    for i in string.ascii_uppercase:
        filename = f"{i}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")
    print("26 text files (A-Z) created.")

gen()