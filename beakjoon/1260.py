# dfs 와 bfs
from collections import deque
import sys
input = sys.stdin.readline

v, e, strNum = map(int, input().split())
graph = [[False]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False]*(v+1)
visited2 = [False]*(v+1)


def dfs(strNum):
    visited1[strNum] = True
    print(strNum, end=" ")
    for i in range(1, v+1):
        if not visited1[i] and graph[strNum][i]:
            dfs(i)
    pass


def bfs(strNum):
    q = deque([strNum])
    visited2[strNum] = True
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, v+1):
            if not visited2[i] and graph[V][i]:
                q.append(i)
                visited2[i] = True
    pass


dfs(strNum)
print()
bfs(strNum)
