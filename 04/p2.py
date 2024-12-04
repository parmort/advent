from typing import List
from dataclasses import dataclass

@dataclass
class Match:
    l: str
    r: str
    center: bool = False

    def __repr__(self):
        if self.center: return f'({self.l}A {self.r}A)'
        else: return f'({self.l} {self.r})'

t_list = List[List[Match]]

def run(lines: List[str]) -> int:
    ans = 0
    n = len(lines[0])
    prev: t_list = [[] for _ in range(n)]

    for line in lines:
        cur: t_list = [[] for _ in range(n)]
        for i,c in enumerate(line):
            match c:
                case 'A':
                    if i in range(1, n-1):
                        for m in prev[i-1]:
                            if m.center: continue
                            cur[i].append(Match(m.l, m.r, True))
                case 'S' | 'M':
                    if i < n-2 and line[i+2] in ['M', 'S']:
                        cur[i].append(Match(c, line[i+2]))

                        for m in prev[i+1]:
                            if not m.center: continue
                            if c != m.r and line[i+2] != m.l: ans += 1

        prev = cur

    return ans
