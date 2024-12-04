import sys
import p1, p2

inp = []
for ln in sys.stdin: inp.append(ln.strip())

print('==MODULE 04==')
print('P1:', p1.run(inp))
print('P2:', p2.run(inp))
