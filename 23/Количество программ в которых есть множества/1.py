def f(x, y, num):
    if x==y: return 1
    if x> y or x==num: return 0
    return f(x+1, y, num) + f(x+2, y, num) + f(x+4, y, num) + f(x+8, y, num)

print((f(16, 24, 32) * f(24, 48, 32)) + (f(16, 32, 24) * f(32, 48, 24)))
