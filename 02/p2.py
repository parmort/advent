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

    for report in lines:
        levels = [int(x) for x in report.split()]

        if isValid(levels): ans += 1
        else:
            safe = False
            for i in range(len(levels)):
                new_lvl = levels.copy()
                del new_lvl[i]
                if isValid(new_lvl):
                    safe = True
                    break

            if safe: ans += 1

    return ans
