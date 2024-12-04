from dataclasses import dataclass
from typing import List

@dataclass
class VertMatch:
    backwards: bool
    len: int = 1
    dir: str|None = None

    def __repr__(self):
        def txt():
            match self.len:
                case 1: return 'S' if self.backwards else 'X'
                case 2: return 'SA' if self.backwards else 'XM'
                case 3: return 'SAM' if self.backwards else 'XMA'
                case _: return ''

        return f'({txt()}, {self.dir})'

    def next(self) -> str:
        match self.len:
            case 1: return 'A' if self.backwards else 'M'
            case 2: return 'M' if self.backwards else 'A'
            case 3: return 'X' if self.backwards else 'S'
            case _: return ''

t_line = List[List[VertMatch]]

def run(lines: List[str]) -> int:
    ans = 0
    n = None
    prev: t_line = []

    for line in lines:
        if not n:
            n = len(line)
            prev = [[] for _ in range(n)]

        cur: t_line = [[] for _ in range(n)]
        match = ''
        for i,c in enumerate(line):
            if i > 0 and prev[i-1]:
                for vm in prev[i-1]:
                    if vm.dir not in ['r', None]: continue

                    if c == vm.next():
                        if vm.len+1 == 4: ans += 1
                        else: cur[i].append(VertMatch(vm.backwards, vm.len+1, 'r'))
            if i < n-1 and prev[i+1]:
                for vm in prev[i+1]:
                    if vm.dir not in ['l', None]: continue

                    if c == vm.next():
                        if vm.len+1 == 4: ans += 1
                        else: cur[i].append(VertMatch(vm.backwards, vm.len+1, 'l'))
            for vm in prev[i]:
                if vm.dir not in ['c', None]: continue

                if c == vm.next():
                    if vm.len+1 == 4: ans += 1
                    else: cur[i].append(VertMatch(vm.backwards, vm.len+1, 'c'))

            match c:
                case 'X':
                    cur[i].append(VertMatch(False))
                    if match == 'SAM': ans += 1
                    match = c
                case 'M':
                    if match in ['X', 'SA']: match = match + c
                    else: match = ''
                case 'A':
                    if match in ['XM', 'S']: match = match + c
                    else: match = ''
                case 'S':
                    cur[i].append(VertMatch(True))
                    if match == 'XMA': ans += 1
                    match = c

        prev = cur

    return ans
