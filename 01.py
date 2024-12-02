import sys
from collections import Counter

l, r = [], []

for line in sys.stdin:
    x, y = map(int, line.split())
    l.append(x)
    r.append(y)

l.sort()
r.sort()
ans = 0

for i in range(len(l)):
    ans += abs(l[i] - r[i])

print("P1", ans)

cr = Counter(r)
ans = 0

for id in l:
    ans += id * cr[id]

print("P2", ans)
