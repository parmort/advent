from collections import defaultdict
from p1 import get_input, is_valid

by_page = defaultdict( lambda: ([], []) )

def merge(pages, l, m, r):
    L = pages[l:m+1]
    R = pages[m+1:r+1]
    
    i, j, k = 0, 0, l

    while i < len(L) and j < len(R):
        if L[i] in by_page[R[j]][0]:
            pages[k] = L[i]
            i += 1
        else:
            pages[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        pages[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        pages[k] = R[j]
        j += 1
        k += 1

def merge_sort(pages, l, r) -> None:
    if l < r:
        m = (l + r) // 2

        merge_sort(pages, l, m)
        merge_sort(pages, m+1, r)
        merge(pages, l, m, r)

def run(lines: list[str]) -> int:
    ans = 0
    rules, updates = get_input(lines)

    for rule in rules:
        by_page[rule[0]][1].append(rule[1])
        by_page[rule[1]][0].append(rule[0])

    for pages in updates:
        if is_valid(pages, rules): continue

        merge_sort(pages, 0, len(pages)-1)

        ans += pages[len(pages) // 2]

    return ans
