def w(a,b):
    for i in range(a,b+1):
        yield str(i**2)
a=int(input())
b=int(input())
print(",".join(w(a,b)))
for j in w(a,b):
    print(j)