def three(lis):
    for i in range(len(lis)-1):
        if lis[i]==3 and lis[i+1]==3:
            print(True)    
            return
    print(False)
three([1, 3, 1, 4])