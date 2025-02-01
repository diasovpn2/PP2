def u(lstt):
    lst = []
    for item in lstt:
        if item not in lst:
            lst.append(item)
    print(lst)
u([1, 2, 2, 3, 4, 4, 5]) 
u([1, 1, 1, 1])
