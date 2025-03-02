def n(a):
    u=0
    l=0
    for c in a:
        if c.isupper():
            u=u+1
        else:
            l+=1
    return u,l
a=input()
u,l=n(a)
print(u,l)

