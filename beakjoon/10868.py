# 덱

from collections import deque
import sys
input = sys.stdin.readline

q = deque()
case = int(input())

for _ in range(case):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push_front':
        q.appendleft(int(cmd[1]))
        pass
    elif cmd[0] == 'push_back':
        q.append(int(cmd[1]))
        pass
    elif cmd[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
            continue
        print(q.popleft())
        pass
    elif cmd[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
            continue
        print(q.pop())
        pass
    elif cmd[0] == 'size':
        print(len(q))
        pass
    elif cmd[0] == 'empty':
        print(0 if q else 1)
        pass
    elif cmd[0] == 'front':
        print(q[0] if q else -1)
        pass
    elif cmd[0] == 'back':
        print(q[-1] if q else -1)
        pass
