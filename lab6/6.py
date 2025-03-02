import os
try:
    p=input()
    m=input()
    it=os.listdir(p)
    if m=="directories":
        result=[i for i in it if os.path.isdir(os.path.join(p,i))]
    elif m == "files":
        result = [i for i in it if os.path.isfile(os.path.join(p, i))]
    else:
        result = it
    for item in result:
        print(item)
except Exception as e:
    print("Ошибка:", e)
