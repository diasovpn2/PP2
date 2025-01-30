def solve(h,l):
    x=(4*h-l)//2 #курицы
    y=h-x #кролики
    if 2*x+4*y!=l:
        print("error")
    else:
        print(x,y)
h=35
l=94
print(solve(h,l))
#x + y =h(количество голов)
#2x + 4y = l(количество ног)