def end(h):
    return h>=125
def moves(h):
    return h+2, h+4, h*2
def p1(h):
    return not end(h) and any(end(x) for x in moves(h))
def v1(h):
    return not end(h) and all(p1(x) for x in moves(h))
def p2(h):
    return not p1(h) and any(v1(x) for x in moves(h))
def v2(h):
    return not v1(h) and all(p1(x) or p2(x) for x in moves(h))

for i in range(1, 125):
    h = i
    # if v1(h):  а)
        # print(h) Ответ: 61
    # if p2(h):  б)
    #     print(h) Ответ: 31 57
    # if v2(h):  в)
    #     print(h) Ответ: 55
