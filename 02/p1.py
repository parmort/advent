from typing import List

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

def run(lines: List[str]) -> int:
    ans = 0

    for line in lines:
        report = [int(x) for x in line.split()]
        prev = report[0]
        incr = report[0] < report[1]

        for lvl in report[1:]:
            if (prev < lvl) != incr: break
            if abs(prev - lvl) not in range(1, 4): break
            prev = lvl
        else:
            ans += 1

    return ans

