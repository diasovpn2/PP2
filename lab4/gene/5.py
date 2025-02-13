def w(x):
    for i in range(x,-1,-1):
        yield i
x=int(input())
for e in w(x):
    print(e)