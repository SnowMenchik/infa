f = open('9 baza')
cnt = 0
for s in f:
    a =list(map(int, s.split()))
    powt = [x for x in a if a.count(x) >  1]
    nepowt = [x for x in a if a.count(x) == 1]
    if max(a) not in powt and len(nepowt) == 3 and len(set(powt)) == 2:
        cnt+=1
print(cnt)
