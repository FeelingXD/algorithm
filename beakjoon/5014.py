# 스타트 링크
from collections import deque


def bfs():
    q = deque()
    q.append(s)
    dist[s] = 1
    while q:
        v = q.popleft()
        if v == g:
            print(dist[g]-1)
            return
        for nv in (v+u, v-d):
            if (0 < nv <= f) and not dist[nv]:
                dist[nv] = dist[v]+1
                q.append(nv)
    print("use the stairs")


f, s, g, u, d = map(int, input().split())

dist = [0]*(f+1)
bfs()
