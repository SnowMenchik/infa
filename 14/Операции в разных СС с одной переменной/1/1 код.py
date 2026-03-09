def lp(x, y):
    s= ''
    while x > 0:
        s = str(x % y) + s
        x //= y
    return s
a = lp(((25**500 * (25**625) + 7) // 128), 5)
print(a.count('4'))