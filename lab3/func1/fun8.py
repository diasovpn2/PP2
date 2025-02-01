def seven(nums):
    if 7 in nums:
        index_7 = nums.index(7)
        count_0 =nums[:index_7].count(0)  
        print(count_0 >= 2)  
        return
    print( False)  
seven([1, 2, 4, 0, 0, 7, 5]) 
seven([1, 0, 2, 4, 0, 5, 7]) 
seven([1, 7, 2, 0, 4, 5, 0])

