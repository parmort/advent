import sys

p1 = 0
p2 = 0

def isValid(report: list[int]):
    prev = report[0]
    incr = report[0] < report[1]

    for lvl in report[1:]:
        if (prev < lvl) != incr: break
        if abs(prev - lvl) not in range(1, 4): break
        prev = lvl
    else:
        return True

    return False

for report in sys.stdin:
    levels = [int(x) for x in report.split()]

    if isValid(levels):
        p1 += 1
        p2 += 1
    else:
        safe = False
        for i, lvl in enumerate(levels):
            new_lvl = levels.copy()
            del new_lvl[i]
            if isValid(new_lvl):
                safe = True
                break

        if safe: p2 += 1

print("P1", p1)
print("P2", p2)
