from typing import List
from re import findall

def result(match):
    a, b = [int(x) for x in match[4:-1].split(',')]
    return a * b

def run(lines: List[str]) -> int:
    ans = 0
    for line in lines:
        matches = findall(r"mul\(\d+,\d+\)", line)
        ans += sum(map(result, matches))

    return ans
