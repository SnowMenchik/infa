def end(h):
    return sum(h) <= 200
def moves(h):
    a, b =h
    return (a-3, b-4), (a-8, b//2), (a//2 + a%2, b-10)
def p1(h):
    return not end(h) and any(end(x) for x in moves(h))
def v1(h):
    return not end(h) and all(p1(x) for x in moves(h))
def p2(h):
    return not p1(h) and any(v1(x) for x in moves(h))
def v2(h):
    return not v1(h) and all(p1(x) or p2(x) for x in moves(h))
for j in range(100, 300):
        h = 110, j
        # if v1(h): а)
        #     print(h) Ответ: 198
        # if p2(h): б)
        #     print(h) Ответ: 208 209
        # if v2(h): в)
        #     print(h) Ответ: 218
