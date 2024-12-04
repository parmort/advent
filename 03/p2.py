from typing import List
from re import findall
from p1 import result

def run(lines: List[str]) -> int:
    ans = 0
    do = True

    for line in lines:
        matches = findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

        for instr in matches:
            match instr:
                case "do()": do = True
                case "don't()": do = False
                case _:
                    if do: ans += result(instr)

    return ans
