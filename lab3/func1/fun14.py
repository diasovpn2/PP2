def p(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print(True)
    else:
        print(False)
def seven(nums):
    if 7 in nums:
        index_7 = nums.index(7)
        count_0 = nums[:index_7].count(0)
        print(count_0 >= 2)
    print(False)
