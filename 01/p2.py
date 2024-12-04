from typing import List
from collections import Counter

def run(l: List[int], r: List[int]) -> int:
    cr = Counter(r)
    ans = 0

    for id in l:
        ans += id * cr[id]

    return ans
