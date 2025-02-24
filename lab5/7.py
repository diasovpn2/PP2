def s(a):
    w = a.split('_')
    c = w[0] + ''.join(word.capitalize() for word in w[1:])
    return c
a = input()
print(s(a))
