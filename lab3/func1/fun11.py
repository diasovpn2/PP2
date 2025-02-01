def p(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print(True)
    else:
        print(False)
p("a madam a")  
p("hello") 
