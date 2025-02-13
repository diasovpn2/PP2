def g(x):
    for i in range(1,x+1):
        yield i**2
x=5
for w in g(x):
    print(w)