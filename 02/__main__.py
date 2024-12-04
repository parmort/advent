from sys import stdin
import p1, p2

inp = []
for ln in stdin: inp.append(ln)

print('==MODULE 02==')
print('P1:', p1.run(inp))
print('P2:', p2.run(inp))
