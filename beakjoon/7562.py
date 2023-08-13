# 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline
answer = 0
moves = [[-2, 1], [-2, -1], [-1, 2], [1, 2],
         [2, 1], [2, -1], [-1, -2], [1, -2]]


def bfs(x, y, target, l):
    q = deque()

    visited = [[False]*l for _ in range(l)]

    q.append(([x, y], 0))
    while q:
        c_pos, depth = q.popleft()  # current pos
        if c_pos == target:
            return depth
        else:
            for move in moves:
                cx, cy = c_pos
                nx, ny = move

                nx += cx
                ny += cy

                if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append(([nx, ny], depth+1))

    return 0


t = int(input())
while t:
    l = int(input())
    x, y = map(int, input().split())

    target = list(map(int, (input().split())))
    answer = bfs(x, y, target, l)

    print(answer)
    t -= 1
