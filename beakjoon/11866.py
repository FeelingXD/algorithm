import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
ret = []

while q:
    q.rotate(-(K-1))
    ret.append(q.popleft())

print("<", end="")
for i in ret:
    if i != ret[-1]:
        print(i, end=", ")
    else:
        print(f'{i}>')
