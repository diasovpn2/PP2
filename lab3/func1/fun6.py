def dis():
    x = input()
    y = x.split()
    rev = ""
    for i in range(len(y)):
        rev = y[i] + " " + rev 
    print(rev.strip())

dis()
