from typing import List

l, r = [], []

def run(lines: List[str]) -> int:
    for line in lines:
        x, y = map(int, line.split())
        l.append(x)
        r.append(y)

    l.sort()
    r.sort()
    ans = 0

    for i in range(len(l)):
        ans += abs(l[i] - r[i])

    return ans
