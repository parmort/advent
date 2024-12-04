from sys import stdin
import p1, p2

inp = []
for ln in stdin: inp.append(ln)

print('==MODULE 01==')
print('P1:', p1.run(inp))
print('P2:', p2.run(p1.l, p1.r))
