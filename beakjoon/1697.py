#숨바꼭질 (bfs)
from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(dist[v])
            break
        for nx in (v-1, v+1, v*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[v]+1
                q.append(nx)


MAX = 10**5
dist = [0]*(MAX+1)
n, k = map(int, input().split())
bfs()
