from typing import List, Tuple

t_rules = List[Tuple[int,int]]

def get_input(lines: List[str]):
    rules, updates = [], []
    at_updates = False

    for line in lines:
        if line == '': at_updates = True
        elif not at_updates:
            a, b = [int(x) for x in line.split('|')]
            rules.append((a, b))
        else:
            updates.append([int(x) for x in line.split(',')])

    return (rules, updates)

def is_valid(pages, rules) -> bool:
    for rule in rules:
        if rule[0] not in pages or rule[1] not in pages: continue

        if pages.index(rule[0]) > pages.index(rule[1]):
            break
    else:
        return True

    return False

def run(lines: List[str]) -> int:
    ans = 0
    rules, updates = get_input(lines)

    for pages in updates:
        if is_valid(pages, rules):
            ans += pages[len(pages) // 2]

    return ans
