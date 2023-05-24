# 결혼식
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
k = int(input())

visited = [False]+[False]*k
graph = defaultdict(list)
for i in range(k):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def bfs(graph, str):
    q = deque()
    q.append([str, 0])
    visited[str] = True
    cnt = 0
    while q:
        v, d = q.popleft()
        if d <= 2:
            cnt += 1
        for i in graph.get(v, []):
            if not visited[i]:
                visited[i] = True
                q.append([i, d+1])

    return cnt-1


print(bfs(graph, 1))
