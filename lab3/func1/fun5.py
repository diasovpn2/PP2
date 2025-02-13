def s():
x=input()
d=[]
for i in range(4):
    for j in range(4):
        if i== j:
            continue
        for q in range(4):
            if q==i or q==j:
                continue
            for w in range(4):
                if w==q or w==i or w==j:
                    continue
                 
print(s())