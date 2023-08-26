# 큐
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    cmd = list(map(str, input().strip().split()))
    match cmd[0]:
        case "push":
            q.append(int(cmd[1]))
        case "front":
            print(q[0] if q else -1)
        case "back":
            print(q[-1] if q else -1)
        case "pop":
            print(q.popleft() if q else -1)
        case "size":
            print(len(q))
        case "empty":
            print(0 if q else 1)
