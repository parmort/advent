import sys
import re

p1 = 0
p2 = 0

def result(match):
    a, b = [int(x) for x in match[4:-1].split(',')]
    return a * b

do = True
for line in sys.stdin:
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    
    for instr in matches:
        match instr:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                ans = result(instr)
                p1 += ans
                if do: p2 += ans

print("P1", p1)
print("P2", p2)
