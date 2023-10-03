# 숨박꼭질 3
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    s, b = map(int, input().split())

    visited = [-1]*100001
    visited[s] = 1
    q = deque([s])
    while q:
        v = q.popleft()
        if v == b:
            return visited[v]-1
        else:
            for nv in (v-1, v+1, 2*v):
                if 0 <= nv <= 100000 and visited[nv] == -1:
                    if nv == 2*v:
                        visited[nv] = visited[v]
                        q.appendleft(nv)
                    else:
                        visited[nv] = visited[v] + 1
                        q.append(nv)

    pass


if __name__ == "__main__":
    print(bfs())
